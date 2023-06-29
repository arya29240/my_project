from django.shortcuts import render
from django.http import HttpResponse
from . models import Place,Team
# Create your views here.


def demo(request):
    # name='india'
    # return render(request,'home.html',{'val':name})
    obj=Place.objects.all()
    new=Team.objects.all()
    content={
        'dict1':obj,
        'dict2':new,
    }
    return render(request, 'index.html',content)


# def addition(request):
#     n1=int(request.GET['num1'])
#     n2=int(request.GET['num2'])
#     result=n1+n2
#     return render(request,'result.html',{'res':result})

# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return HttpResponse('im contact')