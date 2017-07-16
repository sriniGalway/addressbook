from django.db import models


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

    def __unicode__(self):
        return self.address
