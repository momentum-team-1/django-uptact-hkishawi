from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm


# Create your views here.
def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/list_contacts.html",
                  {"contacts": contacts})

def show_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "contacts/show_contact.html", {"contact": contact})

def add_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_contact.html", {"form": form})

def add_address(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)

    if request.method == 'GET':
        form = AddressForm()
    else: 
        form = AddressForm(data=request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.contact = contact 
            address.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_address.html", {
        "form": form,
        "contact": contact
    })

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        form = ContactForm(instance=contact)
    else:
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/edit_contact.html", {
        "form": form,
        "contact": contact
    })


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='list_contacts')

    return render(request, "contacts/delete_contact.html",
                  {"contact": contact})

