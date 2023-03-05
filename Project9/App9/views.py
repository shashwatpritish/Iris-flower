from django.shortcuts import render, HttpResponse, redirect
from App9.models import Data
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

# Create your views here.
def home(request):
    return render(request,'index.html')
def flower(request):
    if request.method == "POST":
        iris = load_iris()
        sepal_length = request.POST.get('sepal_length')
        sepal_width = request.POST.get('sepal_width')
        petal_length = request.POST.get('petal_length')
        petal_width = request.POST.get('petal_width')
        data = Data(sepal_length=sepal_length,sepal_width=sepal_width,petal_length=petal_length,petal_width=petal_width)
        # clf = KNeighborsClassifier()
        # f = iris.data
        # l = iris.target
        # clf.fit(f,l)
        # output = clf.predict([[sepal_length,sepal_width,petal_length,petal_width]])
        # print(output)
        sl = float(data.sepal_length)
        sw = float(data.sepal_width)
        pl = float(data.petal_length)
        pw = float(data.petal_width)
        clf = KNeighborsClassifier()
        f = iris.data
        l = iris.target
        clf.fit(f,l)
        output = clf.predict([[sl,sw,pl,pw]])
        flower = ""
        if output==[0]:
            flower = "Iris Setosa"
        elif output==[1]:
            flower = "Iris Versicolor"
        elif output==[2]:
            flower = "Iris Virginica"
        else:
            flower = "Undefined Flower"
        
        data.save()
    return HttpResponse(flower)
def about(request):
    return render(request,'about.html')