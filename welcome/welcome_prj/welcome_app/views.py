from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def welcome(request):
    name=request.GET['name']
    year=request.GET['year']
    month=request.GET['month']
    day=request.GET['day']

    current_year = 2026
    age = current_year - int(request.GET['year'])




    return render(request, 'welcome.html',
            {
            'name': request.GET['name'],
            'year': request.GET['year'],
            'month': request.GET['month'],
            'day': request.GET['day'],
            'age': age,
            })