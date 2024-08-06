from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home_view(request):

    context = {
        'pages': DATA
    }
    return render(request, 'calculator/home.html', context)

def recipe_view(request):
    recipe = request.GET.get('name')
    portion = request.GET.get('servings')

    if portion == None:
        context = {'recipe': DATA[recipe], 'portion': 1}
    else:
        number = int(portion)
        temp = {}
        print(type(number),number)
        for key, value in DATA[recipe].items():
            temp[key] = round(value * number, 2)
            print('temp', temp)
        context = {'recipe': temp,'portion': portion}


    return render(request, 'calculator/index.html', context)
