from django.shortcuts import render,get_object_or_404
from .models import Country,Patients,User
from django.http import Http404


# Create your views here.

def index(request):
    return render(request, 'covidcases/index.html')
    
def home(request):
    user = get_object_or_404(User, pk=request.POST['username'])
    print(user)
    if(user.password==request.POST['pass']):
        all_countires = Country.objects.all()
        print(all_countires)
        context = {
            'all_countries': all_countires
        }

        return render(request, 'covidcases/home.html', context)
    else:
        raise Http404("wrong username or password")

def details(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    all_patients = country.patients_set.all()
    context = {
        'all_patients': all_patients
    }

    return render(request, 'covidcases/details.html', context)

