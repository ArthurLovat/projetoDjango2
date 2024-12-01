from django2.urls import path
from core.views import index, contato, produto


urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),

]
