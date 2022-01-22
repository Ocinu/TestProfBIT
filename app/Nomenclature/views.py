import time

from django.views.generic import ListView

from .models import Product


class ProductView(ListView):
    model = Product
    template_name = 'index.html'
    paginate_by = 50

    def get_queryset(self):
        time.sleep(2)
        return Product.objects.all().order_by('pk')


class CategoryView(ProductView):
    def get_queryset(self):
        time.sleep(2)
        return Product.objects.filter(category_id=self.kwargs['pk']).order_by('pk')
