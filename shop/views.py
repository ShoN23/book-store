from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from cart.forms import CartAddProductForm
from .models import Category, Product


class AboutView(TemplateView):
    template_name = 'about.html'
    
    def get(self, request, *args, **kwargs): 
        categories = Category.objects.all()  
        context = {'categories': categories}
        return render(request, self.template_name, context)

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products
                   })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form':cart_product_form,
    }
    return render(request,'shop/product/detail.html', context)

