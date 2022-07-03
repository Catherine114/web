from rest_framework.serializers import ModelSerializer
from .models import Projects, Student, Place, Lesson


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'