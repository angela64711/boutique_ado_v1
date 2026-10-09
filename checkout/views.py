from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse("products"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51UOgrQEGcITlxcs2RgHhnDtSqdsgCFV6sNBBCIYJc7nmMDNq28U1Z0fLnQ47CAK5g3gaNbsDUNPfaiB0MF1NNYSj000GEs4aHj",
        "client_secret": "test_client_secret",
    }

    return render(request, template, context)
