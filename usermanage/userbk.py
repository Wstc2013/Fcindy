from django.shortcuts import render_to_response
from django.views.generic import ListView, TemplateView
from usermanage.models import UserProfile
class UserlistView(ListView):
    model = UserProfile
    template_name = 'user/user_list.html'
    paginate_by = 13
    before_index = 6
    after_index = 5

    def get_context_data(self, **kwargs):
        context = super(UserlistView, self).get_context_data(**kwargs)
        context['page_range'] = self.get_page_range(context['page_obj'])
        return context

    def get_page_range(self, page_obj):
        start_index = page_obj.number - self.before_index
        if start_index < 0:
            start_index = 0
        end_index = page_obj.number + self.after_index
        page_range = list(page_obj.paginator.page_range)[start_index:end_index]
        return page_range