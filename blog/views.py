from django.shortcuts import render, get_object_or_404,redirect
from .models import Note
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def notes_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'blog/notes_list.html', {'notes':notes})

@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'blog/note_detail.html', {'note':note})

@login_required   
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

@login_required  
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

@login_required
def note_remove(request, pk):
    post = get_object_or_404(Note, pk=pk)
    post.delete()
    return redirect('notes_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('notes_list')
    else:
        form = UserCreationForm()
        print('working test')
    return render(request, 'blog/signup.html', {'form': form})
