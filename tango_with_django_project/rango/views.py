from django.http import HttpResponse

def index(request): # one view called index ;
    # Each view takes in at least one argument - a HttpRequest object, which also lives in the django.http module.
    # Convention dictates that this is named request, but you can rename this to whatever you want if you so desire
    return HttpResponse("Rango says: Hello world! <a href='/rango/about'>About</a>") # Each view must return a HttpResponse object. A simple HttpResponse object takes a string parameter
    # representing the content of the page we wish to send to the client requesting the view

def about(request):
    return HttpResponse("Rango Says: Here is the about page. <a href= '/rango/'>Index</a>")