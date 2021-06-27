from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('buy/<int:id>', views.buy),
    path('category/<slug>', views.category),
    path('basket/add/<int:id>', views.basket_add),
    path('basket', views.basket),
    path('basket/delete/<int:id>', views.basket_delete),
    path('order', views.order),
    path('order/create', views.order_create),
    path('discount/<int:id>', views.discount),
    path('basket/add_discount/<int:id>', views.basket_add_disk),
    path('basket/delete_discount/<int:id>', views.basket_delete_disk)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


