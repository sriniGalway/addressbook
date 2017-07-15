from django.contrib import admin
from addressbook.models import Entry
 
admin.site.register(Entry)

def clean_email(self):
        try:
            email = self.cleaned_data['email']
            if (self.id):
                User.objects.exclude(id=self.id).get(Q(email=email) | Q(username=email))
            else:
                User.objects.get(Q(email=email) | Q(username=email))
            # here we raise error since it seems that we found an entry...?
            raise forms.ValidationError('That email address (' + email + ') is already registered please try another one.')
        except User.DoesNotExist:
            return email
