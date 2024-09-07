from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'Sportify',
        'name': 'Nabeel Muhammad',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
