from django.shortcuts import render
# from bs4 import BeautifulSoup
from .models import Score
# import pyrebase
# Create your views here.
def index(request):
    return render(request,"index.html")
def game(request):

    return render(request,'game.html')
def submit(request):
    if request.method=="POST":
        
        #----------------------------------initail logic--------------------------------------------
        # a=[request.POST['1'],request.POST['2'],request.POST['3']
        # ,request.POST['4'],request.POST['5'],request.POST['6']
        #     , request.POST['7'],request.POST['8'],request.POST['9']]
        # print(a)
        one=request.POST['winner']
        print(one)
        n1=request.POST['name1']
        n2=request.POST['name2']
        print(n1+"  "+n2)
        #----------------------------------initail logic--------------------------------------------
        # if a[0] == '1' and a[4] == '1' and a[8] == '1' or a[6] == '1' and a[4] == '1' and a[2] == '1' or a[0] == '1' and a[1] == '1' and a[2] == '1' or a[3] == '1' and a[4] == '1' and a[5] == '1' or a[6] == '1' and a[7] == '1' and a[8] == '1' or a[2] == '1' and a[5] == '1' and a[8] == '1' or a[1] == '1' and a[4] == '1' and a[7] == '1' or a[0] == '1' and a[3] == '1' and a[6] == '1':
        # #checking possible 3 1's manually 
        #     win=n1+" winner"
        #     score=Score(Name=n1,Won=True)
        #     score.save()
        #     win=n1+" winner"
        #     score=Score(Name=n2)
        #     score.save()
        #     print("name1")
        # elif ((a[0]=='0' and a[4]=='0' and a[8]=='0') or (a[6]=='0'and a[4]=='0' and a[2]=='0') or (a[0]=='0'and a[1]=='0' and a[2]=='0') or  (a[3]=='0'and a[4]=='0' and a[5]=='0') or (a[6]=='0'and a[7]=='0' and a[8]=='0') or (a[2]=='0'and a[5]=='0' and a[8]=='0') or (a[1]=='0'and a[4]=='0' and a[7]=='0') or (a[0]=='0'and a[3]=='0' and a[5]=='0')):#checking possible 3 0's manually 
        
        #     win =n2+" winner"
        #     score=Score(Name=n2,Won=True)
        #     score.save()
        #     win=n1+" winner"
        #     score=Score(Name=n1)
        #     score.save()
        #     print("name2")

        
        if one=='X':
            win = n1 + " winner"
            score = Score(Name=n1, Won=True)
            score.save()
            score = Score(Name=n2)
            score.save()
            print("name1")
        elif one=='O':
            win = n2 + " winner"
            score = Score(Name=n2, Won=True)
            score.save()
            score = Score(Name=n1)
            score.save()
            print("name2")
        else:
            win="draw match"
        m={"w":win}
        return render(request,'winner.html',m)

def view(request):
    scoreall=Score.objects.all
    msg={
        "scoreall":scoreall
    }
    return render(request,"view.html",msg)