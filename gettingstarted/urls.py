from django.conf.urls import url
from django.urls import path

from django.contrib import admin

import hello.views

admin.autodiscover()

urlpatterns = [
    url(r'^$', hello.views.InvoiceListView.as_view(), name='invoice-list'),
    path('admin/', admin.site.urls),
]
