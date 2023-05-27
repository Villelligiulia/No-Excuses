from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import redirect, get_object_or_404, render
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskForm
from django.contrib import messages


class TaskList(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task.html"
    context_object_name = "tasks"
    login_url = "login"

# Implement a search task function for the user
# if search button clicked with empty task bar inform user
# if search button clicked with not exiting task inform user


class SearchTask(generic.ListView):
    model = Task
    template_name = "task.html"
    context_object_name = "tasks"

    def get_queryset(self):
        query = self.request.GET.get('task')
        tasks = Task.objects.filter(title__icontains=query).order_by('title')
        if not query:
            messages.warning(self.request, 'Please enter a task to search.')
            return tasks
        tasks = Task.objects.filter(title__icontains=query).order_by('title')
        if not tasks:
            messages.warning(self.request, 'No tasks found.')
        return tasks

# Implement Add task funcionality
# and diplay message to the user the task has been added


class AddTask(LoginRequiredMixin, generic.CreateView):
    model = Task
    template_name = "add_task.html"
    form_class = TaskForm
    success_url = reverse_lazy("home")
    login_url = "login"

    def form_valid(self, form):
        messages.success(self.request, "You added a new task")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("home")

# Implement Update task funcionality
# and display message to the user the task has been updated


class UpdateTask(LoginRequiredMixin, generic.UpdateView):
    model = Task
    template_name = "add_task.html"
    form_class = TaskForm
    success_url = reverse_lazy("home")
    login_url = "login"

    def form_valid(self, form):
        messages.success(self.request, "You have updated a task")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("home")

# Implement Delete task view funcionality
# and display message to the user the task has been deleted


class DeleteTask(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "delete_task.html"
    context_object_name = "task_to_delete"

    success_url = reverse_lazy("home")
    login_url = "login"

    def delete(self, request, *args, **kwargs):
        messages.success(request, "You have deleted a task")
        return super().delete(request, *args, **kwargs)

# implement Toggle task funcionality


class ToggleTask(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()
        return redirect("home")

    login_url = "login"
