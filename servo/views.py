import json

from django.http import HttpResponse

from servoctrl import servo

servo = servo()


def index(request):
    #received_json_data = json.loads(request.body)
    if request.GET.get('x'):
        x = request.GET['x']
        print("x = " + x)

    if request.GET.get('y'):
        y = request.GET['y']
        print("y = " + y)

    # if request.GET.get('z'):
    #     z = request.GET['z']
    #     print("z = " + z)

    if y >= 1:
        servo.yServoUp()
    else:
        servo.yServoDown()

    if x >= 1:
        servo.xServoUp()
    else:
        servo.xServoDown()

    return HttpResponse("Hello, world. You're at the polls index.")