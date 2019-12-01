from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'abdarker',
        'title': 'Recyclable',
        'date_posted': 'December 1, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request,'recyclable_app/home.html', context)
    
def about(request):
    return render(request,'recyclable_app/about.html',{'title':'About'})
    
