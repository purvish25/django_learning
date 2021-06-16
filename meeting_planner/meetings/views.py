from django.shortcuts import render, get_object_or_404, get_list_or_404
from meetings.models import Meeting, Room


def detail(request, id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meeting/detail.html", {"meeting": meeting})


def rooms(request):
    rooms = get_list_or_404(Room)
    return render(request, "meeting/rooms_list.html", {"rooms": rooms})
