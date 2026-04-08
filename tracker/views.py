from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LearningEntry
from .serializers import EntrySerializer

@api_view(['GET'])
def api_entries(request):
    entries = LearningEntry.objects.all()
    return Response(EntrySerializer(entries, many=True).data)