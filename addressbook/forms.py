from django import forms

from .models import EntryModel

class EntryForm(forms.ModelForm):
    class Meta:
        model = EntryModel
        fields = ['name', 'surname', 'mobile','email', 'address']

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
