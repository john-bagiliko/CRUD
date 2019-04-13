from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.views.generic import ListView, DetailView

### New home view for posts
class IndexView(ListView):
	template_name='Crud/index.html'
	context_object_name = 'post_list'
	def get_queryset(self):
		return Post.objects.all()

#Detail view (view post detail)
class PostDetailView(DetailView):
	model=Post
	template_name = 'Crud/post-detail.html'

#New post view (Create new post)
def postview(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	form = PostForm()
	return render(request,'Crud/post.html',{'form': form}) 

#Edit a post
def edit(request, pk, template_name='Crud/edit.html'):
    post= get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

#Delete post
def delete(request, pk, template_name='Crud/confirm_delete.html'):
    post= get_object_or_404(Post, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object':post})