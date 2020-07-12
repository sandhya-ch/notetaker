from django.shortcuts import render, get_object_or_404,redirect
from .models import Note
from .forms import NoteForm

# Create your views here.
def notes_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'blog/notes_list.html', {'notes':notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'blog/note_detail.html', {'note':note})
    
def note_new(request):
    if request.method=='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            note=form.save(commit=False)
            note.user=request.user
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form=NoteForm()
    return render(request, 'blog/note_new.html', {'form':form})
   
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method=='POST':
        form=NoteForm(request.POST,instance=note)
        if form.is_valid():
            note=form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form=NoteForm(instance=note)
    return render(request, 'blog/note_new.html', {'form':form})

def note_remove(request, pk):
    post = get_object_or_404(Note, pk=pk)
    post.delete()
    return redirect('notes_list')
