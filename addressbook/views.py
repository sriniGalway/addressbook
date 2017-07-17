from django.contrib.auth.decorators import login_required #for login
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.db.models import Q #for search query

#Avid Media project specific
from .models import EntryModel
from .forms import EntryForm

@login_required(login_url='/admin/login/') #redirect to the login page, if user not logged in
def entries_create_view(request):
    form = EntryForm(request.POST or None)

    context_dictionary = {"form": form} #actual content from form input

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save() #saving the form entry to address book
        messages.success(request, "Successfully created a new entry with id={num}.".format(num=obj.id)) #post message after successfully creating entry
        context_dictionary = {
            "form": EntryForm() #form cleared
        }

    if request.user.is_authenticated():
        template_path = "entries_create.html"

    return render(request,template_path, context_dictionary)


@login_required(login_url='/admin/login/') #redirect to the login page, if user not logged in
def entries_update_view(request, id=None):
    try:
        entry = EntryModel.objects.get(id=id) #get entry by id
    except:
        raise Http404
    form = EntryForm(request.POST or None, instance=entry)
    context_dictionary = {
                "form": form
                } #actual content from form input
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save() #saving the form entry to address book
        messages.success(request, "Successfully updated a new entry with id={num}.".format(num=obj.id)) #post message after successfully creating entry
        return HttpResponseRedirect("/entries/{num}".format(num=obj.id)) #redirct to the updated entry

    if request.user.is_authenticated():
        template_path = "entries_update.html"

    return render(request,template_path, context_dictionary)



@login_required(login_url='/admin/login/')
def entries_delete_view(request, id=None):
    try:
        entry = EntryModel.objects.get(id=id)
    except:
        raise Http404
    if request.method == "POST":
        entry.delete()
        messages.success(request, "Successfully deleted the entry") #post message after successfully deleting entry
        return HttpResponseRedirect("/entries") #redirect to all entries
    context_dictionary = {'entry': entry}

    if request.user.is_authenticated():
        template_path = "entries_delete.html"
    else:
        template_path = "user_not_logged.html"

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
    query = request.GET.get("q")
    print(request.user.username)
    entries_list = EntryModel.objects.filter(user=request.user.username)
    if query is not None:
        entries_list = entries_list.filter(
                Q(name__icontains=query) |
                Q(surname__icontains=query) |
                Q(mobile__icontains=query) |
                Q(email__icontains=query) |
                Q(address__icontains=query)
                ) #search by either of the fields
    context_dictionary = {'entries_list': entries_list}

    if request.user.is_authenticated():
        template_path = "entries_list.html"
    else:
        template_path = "user_not_logged.html"
        #raise Http404
        return HttpResponseRedirect("admin/login/")

    return render(request,template_path, context_dictionary)

@login_required
def entries_for_user(request):
    entry = EntryModel.objects.filter(user=request.user)
    return render(request, 'todos/index.html', {'entry' : entry})
