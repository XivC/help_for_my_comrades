from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from tests.models import Test
from tests.serializers import TestSerializer, DetailedTestSerializer


class TestViewSet(ReadOnlyModelViewSet):
    serializer_classes = {
        'list': TestSerializer,
        'retrieve': DetailedTestSerializer,
    }
    queryset = Test.objects.all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, TestSerializer)

    def get_queryset(self):
        if self.action == 'retrieve':
            return super().get_queryset().prefetch_related('tasks__variants', 'tasks__topic')
        return super().get_queryset()

