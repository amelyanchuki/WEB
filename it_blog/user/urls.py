from django.urls import path
from user.views import signin



urlpatterns = [
    path("singin/", signin, name="signin_page"),
    # path("login/", login, name="login_page"),
    # path("", lambda requset: redirect("/user/login/")),

]

