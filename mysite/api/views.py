from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from polls import views as pollsViews
import json

# Create your views here.

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def MockAPIView(request):
    json_data = json.loads(request.body)
    if 'budget' in json_data:
        if str(json_data["budget"]).isnumeric():
            json_data["budget"] = pollsViews.placeholderFunction(json_data["budget"])
    return Response({"data": json_data["budget"]})

