from django.shortcuts import render

def show_main(request):
    context = {
        'namatoko' : 'Toko Pacil',
        'name': 'Erland Hafizh Aristovi',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
