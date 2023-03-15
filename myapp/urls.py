from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('User', views.UserViewSet)
router.register('Note', views.NoteViewSet)
router.register('PostIt', views.PostItViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index),
    path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login/'),
    path('note/<int:user_id>/make/', views.make_note, name='note_make'),
    path('note/<int:user_id>/edit/', views.edit_note, name='note_edit'),
]