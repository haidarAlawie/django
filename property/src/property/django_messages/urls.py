from django.conf.urls import url
from django.views.generic import RedirectView

from django_messages.views import *






urlpatterns = [
    url(r'^$', RedirectView.as_view(permanent=True, url='inbox/'), name='messages_redirect'),
    url(r'^inbox/$', inbox, name='messages_inbox'),
    url(r'^outbox/$', outbox, name='messages_outbox'),
    url(r'^compose/$', compose, name='messages_compose'),
    url(r'^compose/(?P<recipient>[\w.@+-]+)/$', compose, name='messages_compose_to'),
    url(r'^reply/(?P<message_id>[\d]+)/$', reply, name='messages_reply'),
    url(r'^view/(?P<message_id>[\d]+)/$', view, name='messages_detail'),
    url(r'^delete/(?P<message_id>[\d]+)/$', delete, name='messages_delete'),
    url(r'^undelete/(?P<message_id>[\d]+)/$', undelete, name='messages_undelete'),
    url(r'^trash/$', trash, name='messages_trash'),
]


#         url('', RedirectView.as_view(permanent=True, url='inbox/'), name='messages_redirect'),
#     url('inbox/', inbox, name='messages_inbox'),
#     url('outbox/', outbox, name='messages_outbox'),
#     url('compose/', compose, name='messages_compose'),
#     url('compose/(?P<recipient>/', compose, name='messages_compose_to'),
#     url('^reply/(<message_id>/', reply, name='messages_reply'),
#     url('^view/(<message_id>/', view, name='messages_detail'),
#     url('^delete/<message_id>/', delete, name='messages_delete'),
#     url('^undelete/<message_id>/', undelete, name='messages_undelete'),
#     url('^trash/$', trash, name='messages_trash'),
