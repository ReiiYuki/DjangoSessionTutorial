from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
    url(r'$',views.login_view,name="index"),
    url(r'^register$',views.register_view,name="register_view"),
    url(r'^reg$',views.register,name="register"),
]
