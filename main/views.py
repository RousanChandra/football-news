from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406435894',
        'name': 'Rousan Chandra Syahbunan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context) 