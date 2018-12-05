from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormForm
from .models import FormModel
from django.http import JsonResponse
from django.views.generic.edit import CreateView


def form_views(request):
    if request.method == "POST":
        form = FormForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('form_detail', pk=post.pk)
        else:
            post = get_object_or_404(FormModel, email=form.data['email'])
            response = render(request, 'success.html', {'post': post})
            response.set_cookie(key='PROMO', value=post.pk)
            return response

    else:
        form = FormForm()
    return render(request, 'form.html', {'form': form})


def form_detail(request, pk):
    post = get_object_or_404(FormModel, pk=pk)
    response = render(request, 'success.html', {'post': post})
    response.set_cookie(key='PROMO', value=pk)
    return response
