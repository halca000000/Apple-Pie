from .models import Post

def common(request):
    context = {
        'user_list':Post.objects.all(), 
    }
    return context