from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


# def api_home(request,*args, **kwargs):

#     # #request->HttpRequest ->Django
#     # #print(dir(request))
#     # #request.body
#     # print(request.GET) # URL query params
#     # print(request.POST)
#     # body=request.body #byte string of json data
#     # data={}
#     # try:
#     #     data = json.loads(body) # string of json data -> python dict
#     # except:
#     #     pass
    
#     # print(data)
#     # # data['headers']= request.headers
#     # print(request.headers)
#     # data['params'] = request.GET
#     # data['headers'] =json.dumps(dict(request.headers))
#     # data['content-type']= request.content_type
    
#     model_data = Product.objects.all().order_by("?").first()
#     data={}
#     if model_data:
#         # data['id']=model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         # # model instance (model_data)
#         # # turn a python dict
#         # # return json to my client
#         data = model_to_dict(model_data,fields=['id','title'])     # AGAIN we can do this thing easyly with model to dict and can edit fields as we need
#     return JsonResponse(data)

# Rest framwork theke Response and decorators theke api view import kore json response ke response akare korlei rest framework er api view te convert hoye jabe
@api_view(["POST"])
def api_home(request,*args, **kwargs):

    # instance = Product.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #     #    data = model_to_dict(instance,fields=['id','title','price','sale_price'])     # AGAIN we can do this thing easyly with model to dict and can edit fields as we need
    #     data = ProductSerializer(instance).data


    #-----------------------Now if we want to validate the data -------------------
    
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"Invalid": "Not good data"},status=400)