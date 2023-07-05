from django.shortcuts import render
from .models import *
from math import ceil
# Create your views here.
def Index(request):
    products=Product.objects.all()
    print(products)
    n=len(products)
    nSlides=n//4+ceil((n/4)-(n//4))
    # params={
    #     'product':products,
    #     'no._of_slide':nSlides,
    #     'range':range(1,nSlides)
    # }
    
    allProds=[[products,range(1,nSlides),nSlides],
                    [products,range(1,nSlides),nSlides]]
    params={
        'allProds':allProds
    }
    return render(request,"shop/index.html",params)

def about(request):
    return render(request,"shop/about.html")