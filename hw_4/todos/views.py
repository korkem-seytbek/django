from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

# Главная страница
def index(request):
    return redirect('/todo-lists')

# Список todo-lists
def todo_list_view(request):
    todo_lists = TodoList.objects.all()
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo-lists')
    else:
        form = TodoListForm()
    return render(request, 'todo_list.html', {'todo_lists': todo_lists, 'form': form})

# Детали TodoList
def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, pk=id)
    todos = todo_list.todos.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = todo_list
            todo.save()
            return redirect(f'/todo-lists/{id}')
    else:
        form = TodoForm()
    return render(request, 'todo_list_detail.html', {'todo_list': todo_list, 'todos': todos, 'form': form})

# Удаление TodoList
def delete_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, pk=id)
    todo_list.delete()
    return redirect('/todo-lists')

# Редактирование TodoList
def edit_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, pk=id)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect(f'/todo-lists/{id}')
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'edit_todo_list.html', {'form': form})

# Удаление Todo
def delete_todo(request, id):
    todo = get_object_or_404(Todo, pk=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect(f'/todo-lists/{todo_list_id}')

# Редактирование Todo
def edit_todo(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect(f'/todo-lists/{todo.todo_list.id}')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form})
