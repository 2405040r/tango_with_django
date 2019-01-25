from django.shortcuts import render 

def index(request):
    context_dict = {'boldmessage':"Crunchy, creamy. cookie, candy, cupcake!"}
    # ^ template vars
    # !^ return rendered template to client
    return render(request, 'rango/index.html', context=context_dict)
	
def about(request):
    return render(request, 'rango/about.html')