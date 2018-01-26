from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.http import JsonResponse
from django.forms import model_to_dict
from .models import Lens
# Create your views here.

class AllView(ListView):
    template_name='all.html'
    headline = 'all'
    model = Lens

    def get_queryset(self):
        return super().get_queryset()

class IndexView(ListView):
    template_name = 'index.html'
    headline = 'home'
    model = Lens 
    paginate_by = 12 

def droploadindex(request):
    return render(request, 'droploadindex.html')

def lens(request):
    page = request.GET.get('page')
    size = request.GET.get('size')
    lens_list = Lens.objects.all()
    paginator = Paginator(lens_list, size) # 每页显示 
    try:
        lenses = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        lenses = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        lenses = paginator.page(paginator.num_pages)
    lenses_list = []
    for lens in lenses:
        lens_dict = dict(name=lens.name,description=lens.description,full=lens.full.url,thumb=lens.thumb.url)
        '''
        # 使用model_to_dict()转化的时候ImageSpecField不能被转化
        lens_dict = model_to_dict(lens)
        lens_dict['full'] = lens_dict['full'].url
        lens_dict['thumb'] = lens_dict['thumb'].url
        '''
        lenses_list.append(lens_dict)
    
    return JsonResponse(lenses_list,safe=False)
    #return render(request, 'index.html', {'lenses': lenses})