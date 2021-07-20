from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Este es una aplicación de musica </h1>")
