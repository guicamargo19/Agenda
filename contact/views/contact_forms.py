from django.shortcuts import render

from contact.forms import ContactForm

# Main Page


def create(request):
    if request.method == 'POST':
        context = {
            "site_title": 'Create - ',
            'form': ContactForm(request.POST),
        }
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
