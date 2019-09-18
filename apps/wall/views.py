from django.shortcuts import render,redirect
from django.contrib import messages
from apps.login_reg.models import User
from .models import Messages, Comments

def success(request):
    if "userid" not in request.session:
        return redirect('/')
    else:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "msgs": Messages.objects.all().order_by("-created_at"),
            # "new_message_form": MessageForm(),
        }
        return render(request, "wall/success.html",context)

def post_message(request):
    if request.method == 'POST':
        if request.POST['post_trigger'] == "msg":
            errors = Messages.objects.post_msg_validator(request.POST)
            if len(request.POST['post_message']) < 5:
                for key, value in errors.items():
                    messages.error(request, value, extra_tags="post_message_fail")
            else:
                User.objects.get(id=request.session['userid']).my_messages.create(message=request.POST['post_message'])
        
        elif request.POST['post_trigger'] == "cmt":
            errors = Comments.objects.post_cmt_validator(request.POST)
            if len(request.POST['post_comment']) < 5:
                for key, value in errors.items():
                    messages.error(request, value, extra_tags="post_comment_fail")
            else:
                user = User.objects.get(id=request.session['userid'])
                Messages.objects.get(id=request.POST['message_id']).commented_msg.create(comment=request.POST['post_comment'],user=user)

        elif request.POST['post_trigger'] == "del":
            Comments.objects.get(id=request.POST['comment_id']).delete()
            
        context = {
            "user": User.objects.get(id=request.session['userid']),
            'msgs': Messages.objects.all().order_by("-created_at"),
        }
    return render(request,'wall/wall.html',context)

# def post_comment(request):
#     if request.method == "POST":
#         errors = Comments.objects.post_msg_validator(request.POST)
#         if len(request.POST['post_comment']) < 5:
#             for key, value in errors.items():
#                 messages.error(request, value, extra_tags="post_comment_fail")
#         else:
#             Messages.objects.get(id=request.POST['message_id']).commented_msg.create(comment=request.POST['post_comment'],user=request.session['userid'])
#             #     bound_form = MessageForm(request.POST)
#             # if bound_form.is_valid():
#             #     User.objects.get(id=request.session['userid']).my_messages.create(message=request.POST['post_message'])  
#             context = {
#                 "user": User.objects.get(id=request.session['userid']),
#                 'msgs': Messages.objects.all(),
#             }
#     return render(request,'wall/wall.html',context)

def logout(request):
    request.session.clear()
    return redirect('/')
