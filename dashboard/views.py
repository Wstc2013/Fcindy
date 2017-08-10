# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.views.generic import View

class IndexView(View):

    def get(self, request):
        return render_to_response('index.html')