from decimal import Decimal

from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.views.generic.list import ListView

from .models import Invoice


class InvoiceListView(ListView):
    model = Invoice

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(grand_total=Coalesce(Sum('invoiceitem__total_cost'), Decimal('0')))
        return queryset
