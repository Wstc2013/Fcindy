from django.conf.urls import url
from usermanage import auth
urlpatterns = [
    url(r'^login/$', auth.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth.LogoutView.as_view(), name='logout'),
]