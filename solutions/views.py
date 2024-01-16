from django.db.models import Count, Q, OuterRef
from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from solutions.filters import TestSolutionFilterSet
from solutions.models import TestSolution, TaskSolution
from solutions.serializers import TestSolutionSerializer
from testing.subqueries import SubqueryCount


class StudentSolutionViewSet(ReadOnlyModelViewSet):

    serializer_class = TestSolutionSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filterset_class = TestSolutionFilterSet

    queryset = TestSolution.objects.annotate(
        score=SubqueryCount(
            TaskSolution.objects.filter(solution_id=OuterRef("id"), chosen_variant__is_correct=True)
        ),
        max_score=Count('test__tasks')
    ).select_related('test')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)



