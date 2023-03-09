from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, NoteSerializer, PostItSerializer
from .models import User, Note, PostIt
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


# 회원가입
def signup(request):
        if request.method == "GET":
            return render(request, 'index.html')
        elif request.method == "POST":
            user_email = request.POST['user_email']
            user_pw = request.POST['user_pw']
            

            if User.objects.filter(user_email=user_email).exists():
                return render(request, 'fakeTaecho.html')

            else:
                user = User(
                    user_email = user_email,
                    user_pw = user_pw,
                )
                user.save()
                return render(request, 'realTaecho.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class PostItViewSet(viewsets.ModelViewSet):
    queryset = PostIt.objects.all()
    serializer_class = PostItSerializer