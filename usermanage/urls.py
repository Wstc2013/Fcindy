from django.conf.urls import url
from usermanage import auth, user
urlpatterns = [
    url(r'^login/$', auth.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth.LogoutView.as_view(), name='logout'),
    url(r'^user_list/$', user.UserlistView.as_view(), name='userlist'),
    url(r'^user_add/$', user.UseraddView.as_view(), name='useradd'),

]