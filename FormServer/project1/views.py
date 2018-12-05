from django.shortcuts import render, redirect, get_object_or_404


def pone(request):
    return render(request, 'project1.html')
