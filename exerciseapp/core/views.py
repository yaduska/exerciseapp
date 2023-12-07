from django.shortcuts import render
from customer.models import Customer

# Create your views here.
def home(request):
    customers=Customer.objects.all()
    return render(request,'core/index.html',{'customers':customers})

