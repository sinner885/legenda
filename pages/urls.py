from django.urls import path

from .views import faq

app_name = "pages"

urlpatterns = [
    path("faq/", faq, name="faq"),  # new
]
