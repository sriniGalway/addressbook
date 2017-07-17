from django.contrib.auth import login, get_user_model, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from addressbook.forms import UserCreationForm, UserLoginForm
User = get_user_model()

def home(request):
    if request.user.is_authenticated():
        print(request.user.profile.user)
    response = HttpResponse(content_type='text/html')
    response.content = '''<!DOCTYPE html>
    <html>
        <head>
            <style>h1 {color: black;}</style>
        </head>
        <body>
            <h1>Welcome to the Address Book page</h1>
            <h3>______________________________________________________</h3>
            <h3>ADMINISTRATION ACTIONS</h3>
            <h3>Click <a href="http://127.0.0.1:8000/admin">here</a> for admin page</h3>
            <h3>Click <a href="http://127.0.0.1:8000/register">Register</a> to Register user</h3>
            <h3>Click <a href="http://127.0.0.1:8000/login">Login</a> to login user</h3>
            <h3>Click <a href="http://127.0.0.1:8000/logout">Logout</a> to logout user</h3>
            <h3>______________________________________________________</h3>
            <h3>USER RELATED ACTIONS</h3>
            <h3>Click <a href="http://127.0.0.1:8000/entries/">here</a> for all the entries</h3>
            <h3>Click <a href="http://127.0.0.1:8000/entries/create">here</a> for creating entry</h3>
            <h3>Enter entry id below and Click <a href='' onclick="this.href='http://127.0.0.1:8000/entries/'+document.getElementById('txtbx').value+'/edit'">update</a> for updating entry</h3>
            <input type="text" value="" id="txtbx" />
            <h3>Enter entry id above and Click <a href='' onclick="this.href='http://127.0.0.1:8000/entries/'+document.getElementById('txtbx').value+'/delete'">delete</a> for updating entry</h3>
        </body>
    </html>
    '''

    print(response.status_code)

    return response

def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/login")
    return render(request, "accounts/register.html", {"form":form})

def user_login(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username_ = form.cleaned_data.get('username')
        user_obj = User.objects.get(username__iexact=username_)
        login(request, user_obj)
        return HttpResponseRedirect("/")
    return render(request, "accounts/login.html", {"form":form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")
