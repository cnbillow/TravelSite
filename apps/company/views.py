from django.shortcuts import render

# Create your views here.

def getAboutWe(request):
    """关于我们"""
    if request.method == "GET":
        return render(request, "about.html", {})


def getContact(request):
    if request.method == "GET":
        return render(request, "contact.html", {})