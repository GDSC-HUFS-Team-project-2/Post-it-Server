from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, NoteSerializer, PostItSerializer
from .models import User, Note, PostIt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'index.html')

# 회원가입
def signup(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        user_email = request.POST.get("user_email")
        user_pw = request.POST.get("user_pw")

        if User.objects.filter(user_email=user_email).exists():
            # return render(request, 'fakeTaecho.html')
            return JsonResponse({"status": "email already exists"})

        else:
            user = User(
                user_email = user_email,
                user_pw = user_pw,
            )
            user.save()
            # return render(request, 'realTaecho.html')
            return JsonResponse({"status": "success"})

# def login(request):
#     if request.method == 'POST':
#         user_email = request.POST['user_email']
#         user_pw = request.POST['user_pw']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('note', id=user.id)
#         else:
#             error_message = "Invalid email or password."
#             return render(request, 'login.html', {'error_message', error_message})

#     else:
#         return render(request, 'login.html')

@csrf_exempt
def make_note(request, user_id):
    if request.method == "POST":
        if Note.objects.filter(user_id=user_id).exists():
            return JsonResponse({"status": "Note already exists"})

        try:
            user = User.objects.get(user_id=user_id)
        except:
            return JsonResponse({"status": "User id does not exists"})
        try:
            user_name = request.POST.get("user_name")
            description = request.POST.get("description")
            note = Note(user_id=user, user_name=user_name, description=description)
            note.save()
            return JsonResponse({"status": "success"})
        except:
            return JsonResponse({"status": "error"})
    else: #method == "GET"
        return render(request, 'note_make.html', {'user_id': user_id})

@csrf_exempt
def edit_note(request, user_id):
    if request.method == "POST":
        try:
            user_name = request.POST.get("user_name")
            description = request.POST.get("description")
            note = Note.objects.get(user_id=user_id)
            note.user_name = user_name
            note.description = description
            note.save()
            return JsonResponse({"status": "success"})
        except:
            return JsonResponse({"status": "error"})
    else: #method == "GET"
        if Note.objects.filter(user_id=user_id).exists():
            try:
                return render(request, 'note_edit.html', {'user_id': user_id})
                # note = Note.objects.get(user_id=user_id)
                # return JsonResponse({"status": "success", "user_name": note.user_name, "description": note.description})
            except:
                return JsonResponse({"status": "error"})
        else:
            return JsonResponse({"status": "Note does not exists"})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class PostItViewSet(viewsets.ModelViewSet):
    queryset = PostIt.objects.all()
    serializer_class = PostItSerializer