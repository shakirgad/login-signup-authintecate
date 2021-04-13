from django.urls import path
from .import views

app_name='accounts'

urlpatterns=[
    path('signup/',views.signup ,name='signup'),
    path('profile/',views.myprofile ,name='myprofile'),
    path('profile_edit/',views.myprofile_edit ,name='myprofile_edit'),
    
]
