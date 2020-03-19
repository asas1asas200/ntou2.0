from django.shortcuts import render, redirect, get_object_or_404
from .forms import postForm
from .models import KobePost
from .autoCheck import checkPost
from .facebookPoster import FbPoster
from .postDeleteTokenCreater import createToken
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

def coc(request):
    return render(request, 'coc.html', {})

def about(request):
    return render(request, 'about.html', {})

def postlist(request):
    post = KobePost.objects.all()
    return render(request, 'postlist.html', {'post': post})

def postSystem(request):
    if request.method == "POST":
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.ipAddress = str(getIp(request))
            post.token = str(createToken.token())
            if post.cocPolicy: # check coc policy
                if checkPost.check(post.content) == True: #auto check post
                    post.check = 'True'
                    post.save()
                    #post.postId = FbPoster.poster(post, post.content) #post to facebook
                    #post.checkPosted = 'True'
                    post.save()
                    return redirect('/')
                else:
                    post.save()
                    return redirect('/')
            else:
                messages.warning(request, '請先閱讀並同意行為準則')
    else:
        form = postForm()
    return render(request, 'post.html', {'form': form})

def getIp(request):
    xForwardedFor = request.META.get('HTTP_X_FORWARDED_FOR')
    if xForwardedFor:
        ip = xForwardedFor.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
