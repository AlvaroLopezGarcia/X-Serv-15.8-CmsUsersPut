from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .models import Pages

FORMULARIO = """
    <form action= "/" Method= "POST">
    URL:<br>
    <input type="text" name="name" placeholder= "name"><br>
    <input type="text" name="page" placeholder= "page"><br>
    <input type="submit" value="Enviar">
</form>
"""

def pages (request, numero):
    try:
        page = Pages.objects.get(id=str(numero))
    except Pages.DoesNotExist:
        return HttpResponseNotFound('<h1>' + numero + ' not found</h1>')
    return HttpResponse(page.name + " " + str(page.page))


@csrf_exempt
def barra(request):
    
    if request.method == "POST":
        page = Pages(name = request.POST['name'], page = request.POST['page'])
        page.save()

    lista = Pages.objects.all()
    respuesta = "<ul>"
    for pagina in lista:
        respuesta += '<li><a href= "/pages/' + str(pagina.id) + '">' + pagina.name + "</a>"
    respuesta += "</ul>"
    if request.user.is_authenticated():
        logged = 'Logged in as ' + request.user.username + '. <a href="/logout">Logout</a></br>'
        respuesta = "<html><body><h1>" + logged + FORMULARIO + "</h1><p>"+ respuesta +"</p></body></html>"
    else:
        logged = 'Not logged in. <a href="/login">Login</a>'
        respuesta = "<html><body><h1>" + logged + "</h1><p>"+ respuesta +"</p></body></html>"
    
    return HttpResponse (respuesta)

