from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


#  View para criar um usuário do sistema
def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado")
            return redirect('contact:login')

    context = {
        'form': form,
    }

    return render(
        request,
        'contact/register.html',
        context,
    )


#  View para fazer login no sistema
def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Logado com sucesso!")
            return redirect('contact:index')
        messages.error(request, 'Login inválido.')

    context = {
        'form': form,
    }

    return render(
        request,
        'contact/login.html',
        context,
    )


#  View para fazer logout do usuário
@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')


# View para atualizar um usuário
@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user-update.html',
            {'form': form},
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user-update.html',
            {'form': form},
        )

    form.save()
    messages.success(request, 'Usuário atualizado com sucesso!')
    return redirect('contact:user_update')
