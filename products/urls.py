from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view
from products.views import (
    render_initial_data,
    dynamic_delete_view,
    product_list_view,
    dynamic_lookup_view,
)

app_name = 'products'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('initial/', render_initial_data),
    path('', product_list_view, name='product-list'),
    path('<int:my_id>/', dynamic_lookup_view, name='product-lookup'),
    path('<int:my_id>/delete/', dynamic_delete_view, name='product-delete'),
]