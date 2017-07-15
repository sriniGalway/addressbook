from django.shortcuts import render

from django.shortcuts import render_to_response
from addressbook.models import Entry
 
def entries(request):
    entries_list = Entry.objects.all()
    return render_to_response('entries_list.html', {'entries_list': entries_list})
