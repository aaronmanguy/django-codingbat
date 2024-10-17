from django.contrib import admin
from django.urls import path

from app.views import near_hundred, string_splosion, cat_dog, lone_sum

urlpatterns = [
    path("warmup-1/near-hundred/<int:num>/", near_hundred),
    path("warmup-2/string-splosion/<str:str1>/", string_splosion),
    path("string-2/cat-dog/<str:str2>/", cat_dog),
    path("logic-2/lone-sum/<int:num1>/<int:num2>/<int:num3>/", lone_sum),
    path('admin/', admin.site.urls),
]
