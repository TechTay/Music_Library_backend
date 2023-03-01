from django.shortcuts import render

# Create your views here.
@api_view(['GET', 'POST'])
def song_list(request):

    if request.method == 'GET':

        queryset= songs.objects.all()