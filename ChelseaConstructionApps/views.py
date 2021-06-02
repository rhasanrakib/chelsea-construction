from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from . forms import ContactForm
def home_view(request):
    context = {
        'logo': 'https://via.placeholder.com/500',
        'slide': [
            'https://via.placeholder.com/1500',
            'https://via.placeholder.com/1500',
            'https://via.placeholder.com/1500',
            'https://via.placeholder.com/1500',

        ],
        'company_name': 'Chelsea Construction Company',
        'company_description': 'Since 1997, Chelsea Construction Company have partnered with homeowners, designers and architects to deliver unrivalled construction, renovation and refurbishment services across London and the Home Counties.',
        'services': {
            'description': '''From luxurious bathrooms to sympathetic renovations, choosing Chelsea Construction
            Company guarantees an impressive end product that will satisfy for years to come.''',
            'services_list': [
                {
                    'service_name': 'Refurbishment & Development',
                    'service_image': 'https://via.placeholder.com/1500',
                },
                {
                    'service_name': 'Maintenance Services',
                    'service_image': 'https://via.placeholder.com/1500',
                },
                {
                    'service_name': 'Deployment Services',
                    'service_image': 'https://via.placeholder.com/1500',
                },
            ]
        },
        'approaches':[
            {
                'name':'Independent & Flexible',
                'image':'https://via.placeholder.com/300'
            },
            {
                'name':'Attention to Detail ',
                'image':'https://via.placeholder.com/300'
            },
            {
                'name':'Responsible & Unobtrusive ',
                'image':'https://via.placeholder.com/300'
            },
            {
                'name':'Professionalism ',
                'image':'https://via.placeholder.com/300'
            },
            {
                'name':'Full Project Management Service ',
                'image':'https://via.placeholder.com/300'
            }
        ],
        'banner':[
            'https://via.placeholder.com/1500',
            'https://via.placeholder.com/1500',
            'https://via.placeholder.com/1500',
            'https://via.placeholder.com/1500',
        ],
        'portfolio':[
            {
                'name':'Private Residence | Chelsea',
                'image':'https://via.placeholder.com/300'
            },
            {
                'name':'Private Residence | Belgravia',
                'image':'https://via.placeholder.com/300'
            },
            {
                'name':'Private Residence | Knightsbridge',
                'image':'https://via.placeholder.com/300'
            },
            
        ],
    }
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        # print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfuly Submitted')
            form.clean()
            return HttpResponseRedirect("")
        else:
            messages.warning(request, 'Fail to Submit')
            #return HttpResponseRedirect(request.path_info)
    
    return render(request, "index.html", context)
