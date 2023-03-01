from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def song_list(request):

    songs = Song.objects.all()

    serializer = SongSerializer(songs, many=True)

    return Response(serializer.data)

        