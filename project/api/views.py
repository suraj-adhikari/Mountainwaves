import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def post(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            url=data['url']
            method=data['method']
            api_key=data['api_key']
            data=data['data']
            headers={
                                'Authorization': f'Bearer {api_key}',
                                'Content-Type':'application/json',
                                # 'Host':'api.hubapi.com'

                            }
# we need to check this response
            response = requests.request(method, url=url,headers=headers, data=data)
            print(response)
            return JsonResponse(data,status=200,safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)

    # Extract data from query parameters:http://localhost:8000/?param=value
    if 'param' in request.GET:
        param_value = request.GET.get('param', None)
        print(param_value)
        # If data comes from PARAM in get request
        return JsonResponse({'message': f'Query parameter received: {param_value}'})
    
    return JsonResponse({'message': 'Please make a Post request to this api'}, status=400)
