from urllib.request import Request
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer, PlaceSerializer, LessonSerializer, ProjectsSerializer
from .models import Student, Place, Lesson, Projects
from rest_framework.generics import ListAPIView 
import django_filters.rest_framework
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class GetPlaceView(ListAPIView):
    queryset = Place.objects.filter( Q(study_place_name='Московский Политех') )
    serializer_class = PlaceSerializer

    
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GetStudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name','group']


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    @action(methods=['Delete'], detail=True, url_path='delete') 
    def delProject(self,request, pk=None):
        project=self.queryset.get(id=pk)
        project.delete()
        return Response('Succses')

class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
