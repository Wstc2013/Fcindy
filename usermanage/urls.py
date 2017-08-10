from django.conf.urls import url
from usermanage import auth
urlpatterns = [
    url(r'^$', auth.LoginView.as_view(), name='login'),
]