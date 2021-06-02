
from . forms import ContactForm


def contact_view(request):
    #form = ContactForm()
    context = {
        'footer_logo':'https://via.placeholder.com/500',
        'address': '''Chelsea Construction Company
                     26 Chilworth Street
                     London, W2 6DT''',
        'phone': '+44 (0) 207 706 9995',
        'email': 'enquiries@chelsea-construction.co.uk',
        'instagram': '#',
        'twitter': '#',
        'form': ContactForm(),
    }
    
    
    return {'contact_view': context}
