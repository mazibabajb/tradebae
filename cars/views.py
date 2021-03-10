from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView 
from.models import Car
from.forms import contactform




def home(request):
	return render(request, 'cars/home.html')	

def car(request):
	context = {
	    'cars':Car.objects.all()
	}
	return render(request,'cars/cars.html',context)	
	

class CarListView(ListView):
	model = Car
	template_name = 'cars/cars.html'
	context_object_name = 'cars'
	ordering = ['-created_with']
	paginate_by = 2


class CarDetailView(DetailView):
	model = Car
	



def contact_us(request):
	if request.method == 'POST':
		form = contactform(request.POST)
		if form.is_valid():
			form.save()
			firstname = form.cleaned_data.get('firstname')
			messages.success(request, f'Thank you for contacting us')

	form = contactform()
	return render(request, 'cars/contact.html', {'form': form})		



def about_us(request):
	return render(request, 'cars/about.html')		






	