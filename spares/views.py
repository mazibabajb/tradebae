from django.shortcuts import render



def spares(request):
	return render(request, 'spares/spares.html')	
	

def spare_detail(request):
	return render(request, 'spares/spare_detail.html')	
