from django.shortcuts import render

# Create your views here.


def main(request, *args, **kwargs):
    context = {}
    return render(request, "store/main.html", context)

# View to be rendered when we want to see our STORE.
# This view is referenced in this app's 'urls.py' file.
def store(request):
    context = {}
    return render(request, "store/store.html", context)


# View to be rendered when we want to see our CHECKOUT page.
# This view is referenced in this app's 'urls.py' file.
def checkout(request):
    context = {}
    return render(request, "store/checkout.html", context)


# View to be rendered when we want to see our CART.
# This view is referenced in this app's 'urls.py' file.
def cart(request):
    context = {}
    return render(request, "store/cart.html", context)