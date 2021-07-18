from django.http import Http404
from django.shortcuts import render
from .models import client
from .forms import Search_Form

# Create your views here.
global_files = client.entry('56c3sgivTfyHrEnbi9vBmJ')
homepage_hero = client.asset('2Rlq0E36tgtmPnrE6DCxjT')



def home(request):
    return render(request, 'index.html', {
        'blogs': client.entries(
            {'content_type': 'blogPost', 'include': 3, 'limit': 4}
        ),'projects': client.entries(
            {'content_type': 'project', 'include': 3, 'limit': 4}
        ),'testimonials': client.entries(
            {'content_type': 'testimonial', 'include': 3, 'limit': 6}
        ),'categories': client.entries(
            {'content_type': 'category', 'include': 3}
        ),'global_files': global_files,
        'hero_image' : homepage_hero,
    })

def about(request):
    return render(request, 'about.html', {
        'person': client.entry('4oem3H3VM1DMnC4Vq8fqAS'),'blogs': client.entries({'content_type': 'blogPost','fields.author.sys.id': '4oem3H3VM1DMnC4Vq8fqAS'}),'recognition': client.entries({'content_type': 'recognition', 'include': 3}),'global_files': global_files
    })

def blogs(request):
    return render(request, 'blog.html', {
        'blogs': client.entries(
            {'content_type': 'blogPost', 'include': 3}
        ),'global_files': global_files
    })

def workshop_detail(request, slug):
    try:
        workshops = client.entries(
            {'content_type': 'workshops', 'fields.slug': slug, 'include': 3}
        )[0]
        return render(request, 'workshops.html', {'workshops': workshops,'global_files': global_files})
    except IndexError:
        raise Http404('Workshop not found for slug: {0}'.format(slug))


def blog_by_slug(request, slug):
    try:
        blog = client.entries(
            {'content_type': 'blogPost', 'fields.slug': slug, 'include': 3}
        )[0]
        return render(request, 'blog/post.html', {'blog': blog,'global_files': global_files})
    except IndexError:
        raise Http404('Post not found for slug: {0}'.format(slug))

def projects(request):
    search_term = ''
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Search_Form(request.POST)
        search_term = request.POST['search_term']
        project_list = client.entries({'content_type': 'project', 'include': 3, 'query': search_term})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Search_Form()
        project_list = client.entries({'content_type': 'project', 'order': ['-sys.createdAt', 'sys.id'], 'include': 3})
    return render(request, 'projects.html', {
        'projects': project_list,'global_files': global_files,'form': form,'search_term': search_term
    })

def project_by_slug(request, slug):
    try:
        project = client.entries(
            {'content_type': 'project', 'fields.slug': slug, 'include': 3}
        )[0]
        return render(request, 'projects/project.html', {'project': project,'global_files': global_files})
    except IndexError:
        raise Http404('Project not found for slug: {0}'.format(slug))

def skills(request):
    return render(request, 'skills.html', {
        'skills': client.entries({'content_type': 'skill', 'include': 3}),'global_files': global_files
    })

def categories(request):
    return render(request, 'categories.html', {
        'skills': client.entries(
            {'content_type': 'category', 'include': 3}),'global_files': global_files
    })


def category_by_slug(request, slug):
    try:
        tag = client.entries(
            {'content_type': 'category', 'fields.slug': slug, 'include': 3}
        )[0]
        return render(request, 'category.html', {'tag': tag,'global_files': global_files})
    except IndexError:
        raise Http404('Skill not found for slug: {0}'.format(slug))
