from django.contrib import admin
from django.urls import path, include
from play_with_data.swagger_urls import swagger_urls  # ✅ Import Swagger URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path("A/", include("api_app.urls")),
    path("orders/",include("orders.urls")),
    path("blog/",include("blog.urls"))
]

# ✅ Include Swagger URLs
urlpatterns += swagger_urls
