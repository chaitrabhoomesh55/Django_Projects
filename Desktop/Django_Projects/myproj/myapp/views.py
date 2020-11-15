from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from myapp.models import Register
# from .models import Register
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.http import HttpResponse, JsonResponse



def hi(request):
    return render(request,'myapp/hi.html')
    


def training_domain(request, domain_id):
    return HttpResponse("You are in:", domain_id)

def home(request):
    return render(request, 'index.html')

def about(request):
   return HttpResponse('About Page')

def create(request):
    if request.method=="POST":
        form = forms.Registerform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('success')
            except:
                print('Error')
    else:
        form=forms.Registerform()
        return render(request, 'register.html', {'form': form})



def success(request):
    return render(request, 'success.html')


def random(request):
    data={1: {'name':'Chika', 'email': 'c@gmail.com'}, 2:{'name':'Jones', 'email': 'j@gmail.com'}}
    return JsonResponse(data)

class Registerlist(APIView):
    def get(self, request):
        values = Register.objects.all().values
        serializer = RegisterSerializer(values, many=True)
        return Response(serializer.data)