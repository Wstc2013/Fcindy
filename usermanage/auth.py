from django.shortcuts import render_to_response
from django.views.generic import View

class LoginView(View):

    def get(self, request):
        return render_to_response('auth/login.html')