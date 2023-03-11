from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import ContactForm
from django.shortcuts import render
from django.views.generic import TemplateView


class OnlineShopView(TemplateView):
    template_name = 'internet.html'
    

class EnterprisePortalView(TemplateView):
    template_name = 'korpor.html'
    

class LPView(TemplateView):
    template_name = 'landing-page.html'
    
    
class PortalView(TemplateView):
    template_name = 'portal.html'


class PricesView(TemplateView):
    template_name = 'prices.html'
    
    
class PromoView(TemplateView):
    template_name = 'promo.html'
    
    
class BCView(TemplateView):
    template_name = 'vizitka.html'
    

class IndexView(TemplateView):
    template_name = 'index.html'
    

def contact_form(request):
    contact_template = 'forms/contact_info.html'
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('contacts:index')
    return render(request, contact_template, {'form': form})


    
# def index(request):
#     template = 'index.html'
#     return render(request, template) 