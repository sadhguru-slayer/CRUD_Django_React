from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    projectmanager = serializers.StringRelatedField()
    class Meta:
        model = Project
        fields = ('id','name','start_date','end_date','comments',"status",'projectmanager')


class ProjectManagerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProjectManager
        fields = ('name', 'id')
