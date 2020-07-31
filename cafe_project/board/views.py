from django.shortcuts import render, get_object_or_404, redirect
from .models  import Board
from user.models import CustomUser


def board_read(request) :
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request,'board/read.html',context)

def board_read_one(request, pk) :
    board = get_object_or_404(Board, pk = pk)
    context = { 'board': board } #추가
    return render(request, 'board/read_one.html',context) #추가


def board_create(request) :
    if  request.method == 'POST' and request.session.get('user', False) :#로그인 유저만 사용가능하게
        title = request.POST['title']
        author = get_object_or_404(CustomUser, username=request.session['user'])
        content = request.POST['content']
        board = Board(
            author = author,
            title = title,
            content = content
            )
        board.save()
        return redirect('board_read')
    else:
        return render(request, 'board/create.html')


def delete_board(request, pk):
    board =Board.objects.get(pk=pk)
    board.delete()
    return redirect('board_read') #read 에서 board_read 로 수정했습니다.


def update_board(request,pk) :
        title  = request.POST['title'] 
        # author = request.POST['author'] 이건 제꺼랑 비교하다가 발견했는데 왜 author은 없는지 모르겠습니다,,ㅠ
        content = request.POST['content']
        board =Board.objects.get(pk=pk)
        board.title = title
        # board.author = author 이것도ㅠㅠ
        board.content = content
        board.save()  
        return redirect('board_read')


def pre_update(request, pk):
        board = get_object_or_404(Board, pk = pk)
        context = {"board" : board}
        return render(request, 'board/update.html', context)