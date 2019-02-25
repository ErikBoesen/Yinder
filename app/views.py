from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = dict(
        Yinder=User.objects.order_by('?')[0],
    )
    return render(request, 'index.html', context)
