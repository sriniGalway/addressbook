from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
# addressbook models.
class EntryModel(models.Model):
    id      = models.BigAutoField(primary_key=True)
    name    = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    mobile  = models.CharField(max_length=30,
                                verbose_name='Mobile Number',
                                unique=True,
                                error_messages={
                                "unique": "This Mobile Number is not unique, please try again.",
                                "blank": "This field is cannot be empty, please try again."
                                },
                                help_text='Must be a unique Mobile Number.')
    address = models.CharField(max_length=80)
    email   = models.EmailField(unique=True,
                                error_messages={
                                "unique": "This e-mail address is not unique, please try again.",
                                "blank": "This field is cannot be empty, please try again."
                                },
                                help_text='Must be a unique e-mail address.')
    user = models.CharField(max_length=80)
    #https://docs.djangoproject.com/en/1.11/topics/auth/customizing/

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

USERNAME_REGEX = '^[a-zA-Z0-9]*$'
class MyUser(AbstractBaseUser):
    username = models.CharField(
                max_length=255,
                validators=[
                    RegexValidator(
                        regex = USERNAME_REGEX,
                        message = 'Username must be Alphanumeric"',
                        code = 'invalid_username'
                    )],
                 unique=True,
                )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return str(self.user.username)

    def __unicode__(self):
        return str(self.user.username)

def post_save_user_model_receiver(sender, instance,created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            password2
post_save.connect(post_save_user_model_receiver, sender = settings.AUTH_USER_MODEL)
