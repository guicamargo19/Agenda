from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact


#  View para criar um contato novo
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            "site_title": 'Create - ',
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()  # argumento commit interrompe o save
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
def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':

        form = ContactForm(request.POST, instance=contact)

        context = {
            "site_title": 'Create - ',
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()  # argumento commit interrompe o save
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        "site_title": 'Create - ',
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context,
    )
