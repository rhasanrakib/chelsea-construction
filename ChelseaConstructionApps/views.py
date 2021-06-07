from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from . forms import ContactForm
context = {
        'logo': "/static/images/primary-blue-grey-footer.png",
        'slide': [
            '/static/images/Chelsea-Construction-Portrait-images-3.jpg',
            '/static/images/Chelsea-Construction-Portrait-images-3.jpg',
            '/static/images/Chelsea-Construction-Portrait-images-3.jpg',
            '/static/images/Chelsea-Construction-Portrait-images-3.jpg',

        ],
        'company_name': 'Chelsea Construction Company',
        'company_description': 'Since 1997, Chelsea Construction Company have partnered with homeowners, designers and architects to deliver unrivalled construction, renovation and refurbishment services across London and the Home Counties.',
        'services': {
            'description': '''From luxurious bathrooms to sympathetic renovations, choosing Chelsea Construction
            Company guarantees an impressive end product that will satisfy for years to come.''',
            'services_list': [
                {
                    'service_name': 'Refurbishment & Development',
                    'service_image': '/static/images/120ElginCrescent-14.jpg',
                },
                {
                    'service_name': 'Maintenance Services',
                    'service_image': '/static/images/120ElginCrescent-14.jpg',
                },
                {
                    'service_name': 'Deployment Services',
                    'service_image': '/static/images/120ElginCrescent-14.jpg',
                },
            ]
        },
        'approaches':[
            {
                'name':'Independent & Flexible',
                'image':'/static/images/Icons-Chelsea-Construction-Professional.png'
            },
            {
                'name':'Attention to Detail ',
                'image':'/static/images/Icons-Chelsea-Construction-Professional.png'
            },
            {
                'name':'Responsible & Unobtrusive ',
                'image':'/static/images/Icons-Chelsea-Construction-Professional.png'
            },
            {
                'name':'Professionalism ',
                'image':'/static/images/Icons-Chelsea-Construction-Professional.png'
            },
            {
                'name':'Full Project Management Service ',
                'image':'/static/images/Icons-Chelsea-Construction-Professional.png'
            }
        ],
        'banner':[
            '/static/images/Chelsea-Construction-Portrait-images-3.jpg',
            '/static/images/Chelsea-Construction-Portrait-images-3.jpg',
            '/static/images/Chelsea-Construction-Portrait-images-3.jpg',
            '/static/images/Chelsea-Construction-Portrait-images-3.jpg',
        ],
        'portfolio':[
            {
                'name':'Private Residence | Chelsea',
                'image':'/static/images/120ElginCrescent-14.jpg'
            },
            {
                'name':'Private Residence | Belgravia',
                'image':'/static/images/120ElginCrescent-14.jpg'
            },
            {
                'name':'Private Residence | Knightsbridge',
                'image':'/static/images/120ElginCrescent-14.jpg'
            },
            
        ],
        'history_first_banner_pic':'/static/images/GavriiLux_London_20181106_123456_HR.jpg'
    }
def home_view(request):
    
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

def about_view(request):
    return render(request,'about.html',context)
def contact_view(request):
    return render(request,'contact.html',context)
def portfolio_view(request):
    return render(request,'portfolio.html',context)