from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='products'),
    path('search/', views.search, name='search'),
    # path('search_results/', views.search_results, name='search_results'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's authentication URLs

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
