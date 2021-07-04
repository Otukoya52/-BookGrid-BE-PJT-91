from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Users
from django.contrib.auth.models import User
from django.core.mail import send_mail 
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Users.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.users.save()


#receiver for password reset
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Bookgrid"),
        # message:
        email_plaintext_message,
        # from:
        "devops4zuri@gmail.com",
        # to:
        [reset_password_token.user.email]
    )