import json

from django.http import HttpResponse

from . import servoctrl

servo = servoctrl.servo()


def index(request):
    #received_json_data = json.loads(request.body)
    if request.GET.get('x'):
        x = request.GET['x']
        print("x = " + x)
        x = float(x)
    if request.GET.get('y'):
        y = request.GET['y']
        print("y = " + y)
        y = float(y)
    # if request.GET.get('z'):
    #     z = request.GET['z']
    #     print("z = " + z)

    if y >= 1.0:
        servo.yServoDown()
    elif y < 0:
        servo.yServoUp()

    if x >= 1.0:
        servo.xServoDown()
    elif y < 0:
        servo.xServoUp()

    return HttpResponse("Hello, world. You're at the polls index.")
