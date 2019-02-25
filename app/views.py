from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    context = dict(
        Yinder=User.objects.order_by('?')[0],
    )
    return render(request, 'index.html', context)
