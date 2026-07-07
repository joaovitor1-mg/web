from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    # Pega o termo de busca enviado via GET (ex: ?search=fusca)
    search = request.GET.get('search')

    if search:
        # Filtra carros que contenham o termo no modelo (ignorando maiúsculas/minúsculas)
        cars = Car.objects.filter(model__icontains=search).order_by('model')
    else:
        # Busca todos os carros se não houver pesquisa
        cars = Car.objects.all().order_by('model')

    return render(
        request, 
        'cars.html', 
        {'cars': cars}
    )