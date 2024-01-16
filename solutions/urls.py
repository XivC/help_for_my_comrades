from rest_framework.routers import SimpleRouter

from solutions.views import StudentSolutionViewSet

router = SimpleRouter()

router.register('solutions', StudentSolutionViewSet)

urlpatterns = router.urls
