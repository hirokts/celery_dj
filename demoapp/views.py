from django.shortcuts import render

from .tasks import add


def hello(request):
    result = add.delay(3, 8)
    while not result.ready():
        print('spam')
    print(result.get())
    return render(request, 'hello.html')
