from django.shortcuts import render
from django.http import HttpResponse

import logging

logger = logging.getLogger("logger_name")


def index(request):
    logger.warning("this will be tracked")
    return HttpResponse("Hello, world. You're at the polls index.")

def post_list(request):
    logger.warning()
    return render(request, 'coffeeshop/post_list.html', {})   