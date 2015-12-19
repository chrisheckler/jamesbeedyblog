from django.shortcuts import render
from django.views.generic import CreateView


class BlogHomeView(CreateView):

    """Blog home view
    """

    template_name = 'blog_home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
