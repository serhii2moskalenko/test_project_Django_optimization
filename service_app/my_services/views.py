from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from my_services.models import Subscription
from my_services.serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
