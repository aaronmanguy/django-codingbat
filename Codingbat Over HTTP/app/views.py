from django.http.response import HttpResponse
from django.http.request import HttpRequest

def near_hundred(request: HttpRequest, num) -> HttpResponse:
    if num <= 110 and num >= 90:
        return HttpResponse(True)
    elif  num <= 210 and num >= 190:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
    
def string_splosion(request: HttpRequest, str1) -> HttpResponse:
    result = ""
    for i in range(0, len(str1) + 1, 1):
        result = result + str1[0:i]
    return HttpResponse(result)

def cat_dog(request: HttpRequest, str2) -> HttpResponse:
    return HttpResponse(str2.count("cat") == str2.count("dog"))

def lone_sum(request: HttpRequest, num1, num2, num3) -> HttpResponse:
    sum = 0
    if num1 != num2 and num1 != num3:
        sum += num1
    if num2 != num1 and num2 != num3:
        sum += num2
    if num3 != num1 and num3 != num2:
        sum += num3
    return HttpResponse(sum)