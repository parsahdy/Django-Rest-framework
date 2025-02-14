from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
    return Response(serializer.data)
        #print(data)
        #data = dict(data )
        #json_data_str = json.dumps(data)
    #return HttpResponse(json_data_str, headers={"content-type": "application/json"})



