from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','artist','album','release_date','genre']
        depth = 1
        # super_type = serializers.IntegerField(write_only=True)