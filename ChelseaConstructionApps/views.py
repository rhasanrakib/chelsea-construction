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
                'image':'/static/images/120ElginCrescent-14.jpg',
                'url':'private_residence'
            },
            {
                'name':'Private Residence | Belgravia',
                'image':'/static/images/120ElginCrescent-14.jpg',
                'url':'private_residence'
            },
            {
                'name':'Private Residence | Knightsbridge',
                'image':'/static/images/120ElginCrescent-14.jpg',
                'url':'private_residence'
            },
            
        ],
        'history_first_banner_pic':'/static/images/GavriiLux_London_20181106_123456_HR.jpg',
        'team':[
            {
                'image':'/static/images/andy-langridge-e1467383076913-550x550-1.jpg',
                'name':'Andrew Langridge',
                'designation':'Managing Director',
                'learn_more':'''
                <p>Andrew started in the industry as a carpenter and soon became a site manager for a large construction firm, eventually specialising in high-end refurbishments. After working on several projects, he saw an opportunity to provide bespoke building services for individual clients, designers and architects, always striving to deliver unrivalled quality.</p>
                <p>Since then, Chelsea Construction Company has grown into a company known for their quality and ability to get to the heart of what their clients are looking for. Andrew still oversees every project, and has a hands on role in the day-today running of the business.</p>
                '''
            },
            {
                'image':'/static/images/andy-langridge-e1467383076913-550x550-1.jpg',
                'name':'Andrew Langridge',
                'designation':'Managing Director',
                'learn_more':'''
                <p>Andrew started in the industry as a carpenter and soon became a site manager for a large construction firm, eventually specialising in high-end refurbishments. After working on several projects, he saw an opportunity to provide bespoke building services for individual clients, designers and architects, always striving to deliver unrivalled quality.</p>
                <p>Since then, Chelsea Construction Company has grown into a company known for their quality and ability to get to the heart of what their clients are looking for. Andrew still oversees every project, and has a hands on role in the day-today running of the business.</p>
                '''
            },
            {
                'image':'/static/images/andy-langridge-e1467383076913-550x550-1.jpg',
                'name':'Andrew Langridge',
                'designation':'Managing Director',
                'learn_more':'''
                <p>Andrew started in the industry as a carpenter and soon became a site manager for a large construction firm, eventually specialising in high-end refurbishments. After working on several projects, he saw an opportunity to provide bespoke building services for individual clients, designers and architects, always striving to deliver unrivalled quality.</p>
                <p>Since then, Chelsea Construction Company has grown into a company known for their quality and ability to get to the heart of what their clients are looking for. Andrew still oversees every project, and has a hands on role in the day-today running of the business.</p>
                '''
            },
        ],
        'details_approaches':[
            {
                'bg_image':"/static/images/GavriiLux_London_20181106_112148_HR.jpg",
                'approach_img':"https://www.chelsea-construction.co.uk/wp-content/uploads/2020/09/independent-and-fexible-incon-white.png",
                'description':'''Based in the heart of London, Chelsea Construction Company is an
                    independent business with a commitment to quality, reliability and professionalism. Still run by its
                    founder, we believe that any team is only as good as its members – that’s why we combine our own
                    hugely experienced craftsmen with a trusted supplier network, offering end-to-end construction,
                    renovation and refurbishment services to designers, architects and homeowners alike.''',
                'title':'Independent & Flexible',
            },
            {
                'bg_image':"/static/images/GavriiLux_London_20181106_112148_HR.jpg",
                'approach_img':"https://www.chelsea-construction.co.uk/wp-content/uploads/2020/09/independent-and-fexible-incon-white.png",
                'description':'''Based in the heart of London, Chelsea Construction Company is an
                    independent business with a commitment to quality, reliability and professionalism. Still run by its
                    founder, we believe that any team is only as good as its members – that’s why we combine our own
                    hugely experienced craftsmen with a trusted supplier network, offering end-to-end construction,
                    renovation and refurbishment services to designers, architects and homeowners alike.''',
                'title':'Independent & Flexible',
            },
            {
                'bg_image':"/static/images/GavriiLux_London_20181106_112148_HR.jpg",
                'approach_img':"https://www.chelsea-construction.co.uk/wp-content/uploads/2020/09/independent-and-fexible-incon-white.png",
                'description':'''Based in the heart of London, Chelsea Construction Company is an
                    independent business with a commitment to quality, reliability and professionalism. Still run by its
                    founder, we believe that any team is only as good as its members – that’s why we combine our own
                    hugely experienced craftsmen with a trusted supplier network, offering end-to-end construction,
                    renovation and refurbishment services to designers, architects and homeowners alike.''',
                'title':'Independent & Flexible',
            },
            {
                'bg_image':"/static/images/GavriiLux_London_20181106_112148_HR.jpg",
                'approach_img':"https://www.chelsea-construction.co.uk/wp-content/uploads/2020/09/independent-and-fexible-incon-white.png",
                'description':'''Based in the heart of London, Chelsea Construction Company is an
                    independent business with a commitment to quality, reliability and professionalism. Still run by its
                    founder, we believe that any team is only as good as its members – that’s why we combine our own
                    hugely experienced craftsmen with a trusted supplier network, offering end-to-end construction,
                    renovation and refurbishment services to designers, architects and homeowners alike.''',
                'title':'Independent & Flexible',
            },
            {
                'bg_image':"/static/images/GavriiLux_London_20181106_112148_HR.jpg",
                'approach_img':"https://www.chelsea-construction.co.uk/wp-content/uploads/2020/09/independent-and-fexible-incon-white.png",
                'description':'''Based in the heart of London, Chelsea Construction Company is an
                    independent business with a commitment to quality, reliability and professionalism. Still run by its
                    founder, we believe that any team is only as good as its members – that’s why we combine our own
                    hugely experienced craftsmen with a trusted supplier network, offering end-to-end construction,
                    renovation and refurbishment services to designers, architects and homeowners alike.''',
                'title':'Independent & Flexible',
            },
        ]
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
def approach_view(request):
    return render(request,'approach.html',context)
def service_view(request):
    return render(request,'servicelink.html',context)
def refurbish_view(request):
    return render(request,'service1.html',context)
def maintenance_view(request):
    return render(request,'service2.html',context)
def private_residence_view(request):
    return render(request,'private_residence.html',context)