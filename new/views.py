from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("hey how are you")