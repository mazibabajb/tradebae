from django.shortcuts import render



def accessories(request):
	return render(request, 'accessories/accessories.html')	
	

def accessori_detail(request):
	return render(request, 'accessories/accessori_detail.html')	
