from django.shortcuts import render_to_response
from django.views.generic import ListView, TemplateView
from usermanage.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class UserlistView(ListView):

    model = UserProfile
    template_name = 'user/user_list.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super(UserlistView, self).get(request, *args, **kwargs)


class UseraddView(TemplateView):
    template_name = 'user/user_add.html'