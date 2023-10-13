from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages


#  View para criar um usuário do sistema
def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado")
            return redirect('contact:index')

    context = {
        'form': form,
    }

    return render(
        request,
        'contact/register.html',
        context,
    )
