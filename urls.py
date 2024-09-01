from django.urls import path
from . import views

app_name = 'parcel'

urlpatterns = [
    path('', views.parcel_list, name='parcel_list'),
    path('<int:pk>/receive/', views.receive_parcel, name='receive_parcel'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('parcel/', include('parcel.urls', namespace='parcel')),
]
