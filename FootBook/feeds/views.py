from django.shortcuts import redirect, render, get_object_or_404
from .models import Feed
from .forms import FeedForm
from django.contrib.auth.decorators import login_required

def index(request):
    feeds = Feed.objects.order_by('-posted_at')
    return render(request, "feeds/index.html", {
        'feeds': feeds
    })


@login_required(login_url='login')
def new_post(request):
    form = FeedForm()

    if request.method == 'POST':
        form = FeedForm(request.POST, request.FILES)

        if form.is_valid():
            feed = form.save(commit=False)
            feed.posted_by = request.user.profile            
            form.save()
            print(feed.posted_by)
            # messages.success(request, "Post created successfully.")
            feed.posted_by = request.user.profile
            return redirect('index')

    return render(request, "feeds/form.html", {
        'form': form
    })



def view_post(request, pk):
    feed = get_object_or_404(Feed, pk=pk)
    return render(request, "feeds/postview.html", {
        'feed': feed
    })


def edit_post(request, pk):
    feed = get_object_or_404(Feed, pk=pk)
    form = FeedForm(instance=feed)

    if request.method == 'POST':
        form = FeedForm(request.POST, request.FILES, instance=feed)

        if form.is_valid():
            form.save()
    return render(request, "feeds/form.html", {
        'feed': feed,
        'form': form
    })

def delete_post(request, pk):
    feed = get_object_or_404(Feed, pk=pk)
    feed.delete()
    return redirect('index')
