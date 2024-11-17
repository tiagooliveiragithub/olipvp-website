from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from helpers.rands import slugify_new


class DocumentType(models.TextChoices):
        IMPORTANT = 'important', 'Important'
        GUIDE = 'guide', 'Guide'


class Document(models.Model):
    

    name = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, max_length=255,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='document_created_by'
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='document_updated_by'
    )
    active = models.BooleanField(default=False)

    classification = models.CharField(
        max_length=20,
        choices=DocumentType.choices,
        default=DocumentType.IMPORTANT
    )


    def get_absolute_url(self):
        if not self.active:
            return reverse('home')
        return reverse('documents:view', args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)

        super_save = super().save(*args, **kwargs)

    def __str__(self):
        return self.name
