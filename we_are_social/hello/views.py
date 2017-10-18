from django.shortcuts import render

def get_index(request):
   return render(request, "hello_temp/base.html")