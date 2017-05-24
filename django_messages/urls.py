from django.conf.urls import url
from django.views.generic import RedirectView
from rest_framework import routers

from .views import MesssageViewset

router = routers.SimpleRouter()

router.register(r'', MesssageViewset, base_name='message-view')

urlpatterns = [

]

urlpatterns += router.urls
