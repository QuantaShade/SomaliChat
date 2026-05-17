import json
from django.views.decorators.csrf import csrf_exempt
from ...models import Content
from django.http import JsonResponse

@csrf_exempt
def post(request):
    if request.method == "POST":
        body = json.loads(request.body)
        Content.objects.create(
            title = body['title'],
            img = body['img']
        )
        return JsonResponse({
            "ok": True,
            "msg": "Success"
        })
    
@csrf_exempt
def get(request):

    if request.method == "GET":

        posts = Content.objects.all()

        data = []

        for post in posts:
            data.append({
                "title": post.title,
                "img": post.img
            })

        return {
            "data": data
        }