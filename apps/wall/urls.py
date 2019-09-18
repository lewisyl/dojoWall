from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.success),
    url(r'^logout$', views.logout),
    url(r'^post_message', views.post_message),
    # url(r'^post_comment', views.post_comment),

]