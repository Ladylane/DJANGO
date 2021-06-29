from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse 

from pathlib import Path

# Create your views here.
def index(request):
    # BASE_DIR = Path(__file__).resolve().parent.parent
    # return HttpResponse(Path.joinpath(BASE_DIR,'brigadeiro'))
    return render(request, 'principal/index.html')