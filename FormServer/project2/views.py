from django.shortcuts import render, redirect, get_object_or_404


def ptwo(request):
    return render(request, 'project2.html')
