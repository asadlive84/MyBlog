from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'


# def post_list(request):
#     posts = Post.published.all()
#     paginator = Paginator(posts, 2)
#     page = request.GET.get('page')
#
#     try:
#         posts = paginator.page(page)
#         print(f"Check it try: {posts}")
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#         print(f"Page not an integer: {posts}")
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#         print(f"Empty: {posts}")
#
#     return render(request, 'blog/post/list.html', {'posts': posts, 'page': page})


def post_details(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'blog/post/detail.html', {'post': post, })
