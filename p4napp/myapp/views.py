from django.shortcuts import render
from datetime import datetime

def index(request):
    current_time = datetime.now()
    return render(request, 'myapp/index.html', {'current_time': current_time})

