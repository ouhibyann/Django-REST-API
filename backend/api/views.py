from rest_framework import viewsets, generics
from .serializer import TowerSerializer
from .models import Tower
import django_filters.rest_framework


class TowerViewSet(viewsets.ModelViewSet, generics.ListAPIView):

    # As we got only one view I chose to apply a filter in this view
    # However, creating a class XFilterBackend where filter_queryset is redefined would be more convenient and could be applied to multiple views
    serializer_class = TowerSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['mcc', 'net', 'area', 'cell']

    def get_queryset(self):

        mcc = self.request.query_params.get('mcc', None)
        net = self.request.query_params.get('net', None)
        area = self.request.query_params.get('area', None)
        cell = self.request.query_params.get('cell', None)

        if mcc or net or area or cell:
            # The performance might not be great when some fields are not fullfiled - mcc or net which results in big queries
            queryset = Tower.objects.all().filter(mcc__in=mcc) | \
                       Tower.objects.all().filter(net__in=net) | \
                       Tower.objects.all().filter(area__in=area) |\
                       Tower.objects.all().filter(cell__in=cell)

        else:
            queryset = Tower.objects.all()[:10]  # If None is specified in each fields, we return the 10 first rows for performance issue
        return queryset
