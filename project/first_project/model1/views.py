from django.shortcuts import render
from django.http import HttpResponse
from . models import Board,Topic
# Create your views here.

def home(request):
#     boards = Board.objects.all()
#     boards_names=list()
#     for board in boards :
#         boards_names.append(board.name)
#     response_html = '<br>'.join(boards_names)

#     return HttpResponse(response_html)    


    boards=Board.objects.all()
    topics=Topic.objects.all()
    return render(request,'first.html',{'boards':boards},{'topics':topics})

