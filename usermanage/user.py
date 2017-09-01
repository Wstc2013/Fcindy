from django.shortcuts import render_to_response
from django.views.generic import ListView, TemplateView
from usermanage.models import UserProfile
class UserlistView(ListView):
    model = UserProfile
    template_name = 'user/user_list.html'


class UseraddView(TemplateView):
    template_name = 'user/user_add.html'