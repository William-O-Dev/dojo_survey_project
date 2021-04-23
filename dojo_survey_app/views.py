from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def result(request):
    # print(request.POST)
    if request.method == "GET":
        return redirect('/')
    language = []
    print(request.POST.getlist('language'))
    for languages in request.POST.getlist('language'):
        language.append(languages)
    
    request.session['first_name']=request.POST['first_name']
    request.session['last_name']=request.POST['last_name']
    request.session['email']=request.POST['email']
    request.session['gender']=request.POST['gender']
    request.session['campus']=request.POST['campus']
    request.session['languages']=language
    request.session['comments']=request.POST['comments']
    
    return redirect ('/display_results')

def display_results(request):
    return render(request, 'result.html')
