from django.contrib.auth.decorators import login_required #for login
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

#Avid Media project specific
from .models import EntryModel
from .forms import EntryForm

@login_required(login_url='/admin/login/') #redirect to the login page, if user not logged in
def entries_create_view(request):
    form = EntryForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save() #saving the form entry to address book
        messages.success(request, "Successfully created a new entry with id={num}.".format(num=obj.id)) #post message after successfully creating entry
        context_dictionary = {
            "form": EntryForm(request.POST or None)
        }

    context_dictionary = {"form": form}

    if request.user.is_authenticated():
        template_path = "entries_create.html"

    return render(request,template_path, context_dictionary)


@login_required(login_url='/admin/login/')
def entries_detail_view(request, id=None):
    try:
        entry = EntryModel.objects.get(id=id)
    except:
        raise Http404
    context_dictionary = {'entry': entry}

    if request.user.is_authenticated():
        template_path = "entries_detail.html"
    else:
        template_path = "user_not_logged.html"
        #raise Http404

    return render(request,template_path, context_dictionary)

@login_required(login_url='/admin/login/')
def entries_list_view(request):

    print(request.user)

    entries_list = EntryModel.objects.all()
    context_dictionary = {'entries_list': entries_list}

    if request.user.is_authenticated():
        template_path = "entries_list.html"
    else:
        template_path = "user_not_logged.html"
        #raise Http404
        return HttpResponseRedirect("admin/login/")

    return render(request,template_path, context_dictionary)
