from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#  View para criar um contato novo
@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        context = {
            "site_title": 'Create - ',
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            form.save()
            messages.success(request, 'Contato criado')
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        "site_title": 'Create - ',
        'form': ContactForm(),
    }

    return render(
        request,
        'contact/create.html',
        context,
    )


# View para atualizar o contato criado
@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':

        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            "site_title": 'Create - ',
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Contato atualizado')
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        "site_title": 'Update - ',
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context,
    )


# View para deletar um contato
@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'no':
        messages.warning(
            request,
            'Para remover o contato, clique em Confirm'
        )

    if confirmation == 'yes':
        contact.delete()
        messages.error(request, 'Contato apagado')
        return redirect("contact:index")

    context = {
        "site_title": 'Delete - ',
        'confirmation': confirmation,
        'contact': contact,
    }

    return render(
        request,
        'contact/contact.html',
        context,
    )
