from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import ContactForm
from .models import Contact


class OnlineShopView(TemplateView):
    template_name = "internet.html"


class EnterprisePortalView(TemplateView):
    template_name = "korpor.html"


class LPView(TemplateView):
    template_name = "landing-page.html"


class PortalView(TemplateView):
    template_name = "portal.html"


class PricesView(TemplateView):
    template_name = "prices.html"


class PromoView(TemplateView):
    template_name = "promo.html"


class BCView(TemplateView):
    template_name = "vizitka.html"


class IndexView(TemplateView):
    template_name = "index.html"


def create_contact(request):
    contact_template = "includes/contact_info.html"
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("contacts:index")
    return render(request, contact_template, {"form": form})
