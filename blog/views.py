from django.shortcuts import render
from .models import Note

# Create your views here.
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'blog/notes_list.html', {'notes':notes})
