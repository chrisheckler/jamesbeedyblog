from django.conf.urls import url
from django.conf.urls import include
from views import BlogHomeView

urlpatterns = [

    url(r'', BlogHomeView.as_view(), name='blog_home'),
]
