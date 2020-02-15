from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseForbidden
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from datetime import datetime

from mysite.models import Photo


def hello(request):
    return HttpResponse('Hello, World! gizka')


def register(request):
    parsed = json.loads(request.body)

    username = parsed['username']
    password = parsed['password']

    if User.objects.filter(username=username).exists():
        return HttpResponseBadRequest('zle')

    user = User.objects.create_user(username, None, password)

    return HttpResponse('Hello, World user id is: ' + str(user.id))


def logging(request):
    parsed = json.loads(request.body)

    userData = parsed['user']
    username = userData['username']
    password = userData['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('zalogowano')
    else:
        return HttpResponseForbidden('Zle wprowadzone dane!')


@login_required
def my_profile(request):
    user = request.user
    response = {"username": user.username}
    return JsonResponse(response)


@login_required
def add_photo(request):
    parsed = json.loads(request.body)

    photoData = parsed['photoA']
    description = photoData['description']

    photo = Photo(author=request.user, description=description,
                  created=datetime.now())
    photo.save()
    return JsonResponse({'photoId': photo.id})
