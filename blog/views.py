from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404

# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from .models import Post
from .forms import EmailPostForm

# def post_list(request):
#     post_list = Post.published.all()
#     paginator = Paginator(post_list, 3)
#     page_number = request.GET.get('page', 1)
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request, "blog/post_list.html", {"posts": posts})


class PostListView(ListView):
    """
    Альтернативное представление списка постов
    """

    queryset = Post.published.all()  # model=Post -> Post.objects.all()
    context_object_name = "posts"  # objects_list
    paginate_by = 3
    template_name = "blog/post_list.html"


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post_detail.html", {"post": post})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['name']}'s comments: {cd['comments']}"
            send_mail(subject, message, "ingopogreb@gmail.com", [cd["to"]])
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request, "blog/post_share.html", {"post": post, "form": form, "sent": sent}
    )
