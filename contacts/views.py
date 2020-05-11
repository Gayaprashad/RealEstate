from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def contact (request):
    if(request.method=='POST'):
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        #checking if the user has already made an inquiry
        if request.user.is_authenticated:
            user_id= request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact= Contact(listing=listing, listing_id= listing_id, name= name, phone= phone, email=email, message=message,user_id=user_id)

        contact.save()

        #Send Email

        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for '+listing+'. Sign into the admin panel for more inquiry.',
            'deepforce.galaxy@gmail.com',
            [realtor_email, 'deepforce.galaxy@gmail.com']
        )
        
        messages.success(request, 'Your message has been registered')
        return redirect('/listings/'+listing_id)

