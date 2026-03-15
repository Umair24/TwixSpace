from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm, CustomLoginForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    query = request.GET.get('query')

    if query:
        tweets = Tweet.objects.filter(
            Q(text__icontains = query) |
            Q(user__username__icontains = query)
        ).order_by('-created_at')

    return render(request, "tweet_list.html", {'tweets':tweets})


@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form':form})



@login_required
def tweet_edit(request, tweet_id):  # tweet_edit requires an id to allowthe user to edit the tweet

    # let acces to edit tweet if user is logged in
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)    # "User" are current logged in user So only the owner can edit the tweet

    # if request.method is equal to 'POST' then only gave the permission to the user to edit the twwet 
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False) #it will save the tweet but dont save tweet to the server bcz commit = False
            tweet.user = request.user   
            tweet.save()
            return redirect('tweet_list') # it will redirect the user to the main tweet_create.html page after the editing of tweet
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})



@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet':tweet})
    

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form':form})


@login_required
def like_twix(request, tweet_id):
    tweet = get_object_or_404(Tweet, id= tweet_id)

    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)
    
    return redirect("tweet_list")


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "registration/login.html"