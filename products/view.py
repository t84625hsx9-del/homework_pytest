from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .model import Product
from django.urls import reverse_lazy

class ProductCreateView(CreateView):
    template_name='products/create.html'
    success_url=reverse_lazy('product_list')
    model=Product
    fields=['name','price','description','stock']

class ProductListView(ListView):
    model=Product
    template_name='products/list.html'
    context_object_name = 'products'

class ProductDeleteView(DeleteView):
    template_name='products/delete.html'
    success_url=reverse_lazy('product_list')
    model=Product

class ProductUpdateView(UpdateView):
    template_name='products/update.html'
    success_url=reverse_lazy('product_list')
    model=Product
    fields=['name','price','description','stock']