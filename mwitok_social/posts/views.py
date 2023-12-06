from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    post = get_object_or_404(Post, pk=1)
    return render(request, 'posts/index.html', {'post':post})