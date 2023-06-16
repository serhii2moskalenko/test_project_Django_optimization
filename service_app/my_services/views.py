from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from my_services.models import Subscription
from my_services.serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    # queryset = Subscription.objects.all().prefetch_related('client').prefetch_related('client__user')
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client',
        queryset=Client.objects.all().select_related('user').only('company_name',
                                                    'user__email'))
    )
    serializer_class = SubscriptionSerializer
