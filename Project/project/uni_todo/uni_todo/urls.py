from django.urls import include, path

urlpatterns = [
    path('', include("app.urls")),
    path('api/', include("api.urls"))
]
