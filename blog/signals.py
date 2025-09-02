import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import CustomUser, Post

# Delete old avatar when user updates it
@receiver(pre_save, sender=CustomUser)
def delete_old_avatar(sender, instance, **kwargs):
    if not instance.pk:
        return  # New user, no old avatar

    try:
        old_avatar = CustomUser.objects.get(pk=instance.pk).avatar
    except CustomUser.DoesNotExist:
        return

    new_avatar = instance.avatar
    if old_avatar and old_avatar != new_avatar and os.path.isfile(old_avatar.path):
        os.remove(old_avatar.path)

# Delete old post image when updated
@receiver(pre_save, sender=Post)
def delete_old_post_image(sender, instance, **kwargs):
    if not instance.pk:
        return  # New post

    try:
        old_image = Post.objects.get(pk=instance.pk).image
    except Post.DoesNotExist:
        return

    new_image = instance.image
    if old_image and old_image != new_image and os.path.isfile(old_image.path):
        os.remove(old_image.path)
