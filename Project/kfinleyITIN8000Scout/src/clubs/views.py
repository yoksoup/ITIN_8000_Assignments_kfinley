"""
------------------------------------------------------------
Contains most of the functions for the website. This are called in the
{root}/settings.py

club_create_view # creates a new club
club_update_view # allows edit of existing club
club_list_view   # displays a list of clubs
club_detail_view # displays full details (not implemented)
club_delete_view # allows deletion of club by id (not working)
dynamic_lookup_view # allows to look up club by id

------------------------------------------------------------
"""


from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClubForm
from .models import Club

def club_create_view(request):
    form = ClubForm(request.POST or None)
    # checks form to be valid
    if form.is_valid():
        form.save()
        form = ClubForm()
    context = {
        'form': form
    }
    return render(request, "clubs/club_create.html", context)


def club_update_view(request, id=id):
    # gets a 404 error of page not there
    obj = get_object_or_404(Club, id=id)
    form = ClubForm(request.POST or None, instance=obj)
    # checks form to be valid
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "clubs/club_create.html", context)


def club_list_view(request):
    queryset = Club.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "clubs/club_list.html", context)

def club_detail_view(request, id):
    # gets a 404 error of page not there
    obj = get_object_or_404(Club, id=id)
    context = {
        "object": obj
    }
    return render(request, "clubs/club_detail.html", context)


def club_delete_view(request, id=id):
    obj = get_object_or_404(Club, id=id)
    # POST request
    if request.method == "POST":
        # confirms delete
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "clubs/club_delete.html", context)


def dynamic_lookup_view(request, id):
    # gets a 404 error of page not there
    obj = get_object_or_404(Club, id=id)
    context = {
        "object": obj
    }
    return render(request, "clubs/club_detail.html", context)