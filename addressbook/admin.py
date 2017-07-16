from django.contrib import admin
from addressbook.models import EntryModel

admin.site.register(EntryModel)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'mobile', 'address', 'email')

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(EntryAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return EntryModel.objects.all()
        return EntryModel.objects.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()


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
