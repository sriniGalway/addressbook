from django.http import HttpResponse, HttpResponseRedirect

def home(request):

    response = HttpResponse(content_type='text/html')
    response.content = '''<!DOCTYPE html>
    <html>
        <head>
            <style>h1 {color: black;}</style>
        </head>
        <body>
            <h1>Welcome to the Address Book page</h1>
            <h3>Click <a href="http://127.0.0.1:8000/admin">here</a> for admin page</h3>
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
