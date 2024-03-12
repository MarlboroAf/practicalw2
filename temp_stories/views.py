from django.shortcuts import render

def index(request):
    mystory = story()
    converted_t = None
    temp = None
    if request.method== "POST":
        temp = int(request.POST.get('temp',''))
        converted_t = (temp-32)*0.5556
    return render(request, 'temp_stories/index.html', {'story': mystory, 'converted_t': converted_t, 'temp': temp})