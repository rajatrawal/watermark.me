from django.urls import path
from . views import api,watermark_image,sign_in,sign_out,sign_up
urlpatterns = [
    path('api/',api,name="api"),
    path('api/watermarkImage/',watermark_image,name="watermark_image"),
    path('signIn/',sign_in,name='sign_in'),
    path('signOut/',sign_out,name='sign_out'),
    path('signUp/',sign_up,name='sign_up'),
    
]
