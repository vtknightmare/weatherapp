# weather/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MeasureView, CheckView

urlpatterns = {
    url(r'^weather/$', MeasureView.as_view(), name="measure"),
    url(r'^weather/(?P<pk>[0-9]+)/$', CheckView.as_view(), name="check")
}

urlpatterns = format_suffix_patterns(urlpatterns)
