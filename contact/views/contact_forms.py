from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator


# Main Page
def create(request):
    context = {
        "site_title": 'Create - '
    }
    return render(
        request,
        'contact/create.html',
        context,
    )
