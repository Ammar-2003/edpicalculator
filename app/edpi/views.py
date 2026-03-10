from django.shortcuts import render

# Create your views here.
def edpi_calculator(request):
    return render(request , 'edpi_calculator.html')
# Create your views here.
def what_is_edpi(request):
    return render(request , 'what_is_edpi.html')