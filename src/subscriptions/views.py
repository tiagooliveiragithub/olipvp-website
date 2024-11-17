import helpers.billing
import helpers.minecraft
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from subscriptions.models import SubscriptionPrice, UserSubscription
from subscriptions import utils as subs_utils

@login_required
def user_subscription_view(request,):
    user_sub_obj, created = UserSubscription.objects.get_or_create(user=request.user)
    if request.method == "POST":
        print("refresh sub")
        finished = subs_utils.refresh_active_users_subscriptions(user_ids=[request.user.id], active_only=False)
        if finished:
            messages.success(request, "Your plan details have been refreshed.")
        else:
            messages.error(request, "Your plan details have not been refreshed, please try again.")
        return redirect(user_sub_obj.get_absolute_url())
    return render(request, 'main/user_detail_view.html', {"subscription": user_sub_obj, "title": "Subscription Details"})


@login_required
def user_subscription_cancel_view(request,):
    user_sub_obj, created = UserSubscription.objects.get_or_create(user=request.user)
    if request.method == "POST":
        if user_sub_obj.stripe_id and user_sub_obj.is_active_status:
            sub_data = helpers.billing.cancel_subscription(
                user_sub_obj.stripe_id, 
                reason="User wanted to end", 
                feedback="other",
                cancel_at_period_end=True,
                raw=False)
            for k,v in sub_data.items():
                setattr(user_sub_obj, k, v)
            user_sub_obj.save()
            messages.success(request, "Your plan has been cancelled.")
        return redirect(user_sub_obj.get_absolute_url())
    return render(request, 'main/user_cancel_view.html', {"subscription": user_sub_obj, "title": "Cancel Subscription"})


def subscription_price_view(request, interval="month"):
    qs = SubscriptionPrice.objects.filter(featured=True)
    inv_mo = SubscriptionPrice.IntervalChoices.MONTHLY
    inv_yr = SubscriptionPrice.IntervalChoices.YEARLY

    if interval == inv_yr:
        object_list = qs.filter(interval=inv_yr)
    else:
        object_list = qs.filter(interval=inv_mo)

    mo_url = reverse("pricing_interval", kwargs={"interval": inv_mo})
    yr_url = reverse("pricing_interval", kwargs={"interval": inv_yr})

    context = {
        "subscriptions": object_list,
        "mo_url": mo_url,
        "yr_url": yr_url,
        "title": "Members",
        "transition": False,
    }

    if request.headers.get('HX-Request'):

        context = {
            "subscriptions": object_list,
            "mo_url": mo_url,
            "yr_url": yr_url,
            "title": "Members",
            "transition": True,
        }

        return render(request, "subscriptions/subscription_card.html", context)
    
    return render(request, "subscriptions/pricing.html", context)


def post_subscription_minecraft_user(request):
    if request.method == "GET":
        user_sub_obj, created = UserSubscription.objects.get_or_create(user=request.user)
        
        helpers.minecraft.rcon_command(username=user_sub_obj.user.username, plan=user_sub_obj.subscription.subtitle)
        messages.success(request, "Your subscription has been updated.")
        return redirect("user_subscription")
        
    return redirect("user_subscription")

