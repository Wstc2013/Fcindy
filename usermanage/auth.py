#-*-coding:utf8-*-
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginView(View):

    def get(self, request):
        ret = {'message': '', 'next_url': '/'}
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('index'))
        elif request.GET.has_key('next'):
            ret['next_url'] = request.GET['next']
        return render_to_response('auth/login.html', ret)

    def post(self,request):
        ret = {'message': '', 'next_url': '/'}
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        next_url = request.POST.get('next', None)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(next_url)
            else:
                ret['message'] = '用户名被禁用'
        else:
                ret['message'] = '用户名或密码不正确'
        return render_to_response('auth/login.html', ret)


class LogoutView(View):
    @method_decorator(login_required)
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('login'))