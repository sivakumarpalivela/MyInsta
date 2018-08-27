from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'AppBasic'

urlpatterns = [
    path('Home/',views.index,name ='Home'),
    path('',views.index,name = "newhome"),
    path('SignUp/',views.SignUp,name = 'SignUp'),
    path('Login/',views.user_login,name = 'user_login'),
    path('LogOut/',views.LogOut,name = 'logout'),
    path('Post/',views.postmedata,name = 'PostHere'),
    path('Contributions',views.contribute,name = 'Contributions')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)