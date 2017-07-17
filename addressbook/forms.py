from django import forms

from .models import EntryModel

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model, authenticate
from django.core.validators import RegexValidator
from .models import USERNAME_REGEX

User = get_user_model()

class EntryForm(forms.ModelForm):
    class Meta:
        model = EntryModel
        fields = ['name', 'surname', 'mobile','email', 'address', 'user']

    def clean_email(self):
        try:
            email = self.cleaned_data['email']
            if not "com" in email:
                raise forms.validationError("please use a valid .COM email address")

            if (self.id):
                User.objects.exclude(id=self.id).get(Q(email=email) | Q(username=email))
            else:
                User.objects.get(Q(email=email) | Q(username=email))
            # here we raise error since it seems that we found an entry...?
            raise forms.ValidationError('That email address (' + email + ') is already registered please try another one.')
        except:
            return email


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(
                label='username',
                validators=[
                    RegexValidator(
                        regex = USERNAME_REGEX,
                        message = 'Username must be Alphanumeric"',
                        code = 'invalid_username'
                    )])
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        the_user = authenticate(username=username, password=password)
        if not the_user:
            raise forms.ValidationError("Invalid credentials")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username','email', 'password', 'is_staff','is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
