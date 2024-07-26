from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"), 
    path("<int:question_id>/chat/", views.detail, name="chat"),
    path("<int:question_id>/addchoice/", views.addchoice, name="addchoice"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("<int:question_id>/results/", views.results, name="results"),
    
    path('login/', auth_views.LoginView.as_view(
        template_name='polls/login.html'
        ), name='login'),
    
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    
    path("signup/", views.signup, name='signup'),
    
    path('password_change/', auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy('polls:password_change_done')
        ), name='password_change'),
    
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='polls/password_changed.html'
    ), name="password_change_done"),
]
