from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaceViewSet, LessonViewSet, StudentViewSet, ProjectsViewSet, GetStudentView, GetPlaceView
router = DefaultRouter()
router.register('place', PlaceViewSet, )
router.register('lesson', LessonViewSet )
router.register('proj', ProjectsViewSet )
router.register('student', StudentViewSet )




urlpatterns = [
    path('api/', include(router.urls)),
    path('api/place/filter', GetPlaceView.as_view()),
    path('api/student/filter', GetStudentView.as_view()),
]
