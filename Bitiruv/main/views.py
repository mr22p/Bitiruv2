from django.shortcuts import render, get_object_or_404, redirect
from .models import Graduate, AccessCode


def access_login(request):
    if request.method == "POST":
        code = request.POST.get("code")
        if AccessCode.objects.filter(code=code).exists():
            request.session['access_granted'] = True
            return redirect('home')

    return render(request, 'access_login.html')


def home(request):
    if not request.session.get('access_granted'):
        return redirect('access_login')

    graduates = Graduate.objects.all()
    return render(request, 'home.html', {'graduates': graduates})


def graduate_detail(request, pk):
    graduate = get_object_or_404(Graduate, pk=pk)
    projects = graduate.projects.all()

    return render(request, 'detail.html', {
        'graduate': graduate,
        'projects': projects
    })