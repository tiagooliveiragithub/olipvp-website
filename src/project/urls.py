from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from subscriptions import views as subscriptions_views
from checkouts import views as checkout_views
from main import views as main_views
from django.conf.urls import handler404

handler404 = 'main.views.custom_404_view'

urlpatterns = [
    path('', main_views.home, name='home'),
    path('', include('main.urls')),
    path('blog/', include('blog.urls')),
    path('docs/', include('documents.urls')),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('staff/', admin.site.urls, name='staff'),
    

    path('accounts/billing/', subscriptions_views.user_subscription_view, name='user_subscription'),
    path('accounts/billing/cancel', subscriptions_views.user_subscription_cancel_view, name='user_subscription_cancel'),

    path("pricing/", subscriptions_views.subscription_price_view, name='pricing'),
    path("pricing/<str:interval>/", subscriptions_views.subscription_price_view, name='pricing_interval'),

    path("checkout/sub-price/<int:price_id>/", 
            checkout_views.product_price_redirect_view,
            name='sub-price-checkout'
            ),
    path("checkout/start/", 
            checkout_views.checkout_redirect_view,
            name='stripe-checkout-start'
            ),
    path("checkout/success/", 
            checkout_views.checkout_finalize_view,
            name='stripe-checkout-end'
            ),

        # Minecraft
        path("vip/subscribe/", subscriptions_views.post_subscription_minecraft_user, name='vip-subscribe'),

        
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    