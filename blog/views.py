from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Post, Rating, Restaurant

# Create your views here.

def index(request):
    posts = Post.objects.all()
    ratings = Rating.objects.all()
    restaurants = Restaurant.objects.all()
    template = loader.get_template('index.html')
    context = {
        'posts' : posts,
        'ratings' : ratings,
        'restaurants' : restaurants,
    }
    return HttpResponse(template.render(context,request))

#def about(request):
#    template = loader.get_template('about.html')
#    return HttpResponse(template.render())

#def contact(request):
#    template = loader.get_template('contact.html')
#    return HttpResponse(template.render())

def restaurants(request):
    template = loader.get_template('restaurants.html')
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants' : restaurants,
    }
    restaurants = Restaurant.objects.order_by('name')
    return HttpResponse(template.render(context,request))

def view_restaurant(request, name):
    try:
        restaurant = Restaurant.objects.get(name=name)
        rating = restaurant.rating_info
        post = Post.objects.get(rating_info=rating)
        context = {
            'restaurant' : restaurant,
            'rating' : rating,
            'post' : post,
        }
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant doesn't exist")
    return render(request, 'view_restaurant.html', context)


def view_post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        rating = post.rating_info
        score = rating.score
        context = {
            'post' : post,
            'rating' : rating,
            'score' : score,
        }
    except Post.DoesNotExist:
        raise Http404("Post doesn't exist")
    return render(request, 'view_post.html', context)

def view_rating(request, rating_id):
    try:
        rating = Rating.objects.get(pk=rating_id)
        post = Post.objects.get(rating_info=rating)
        context = {
            'rating' : rating,
            'post' : post,
        }
    except Rating.DoesNotExist:
        raise Http404("Rating does not exist")
    return render(request, 'view_rating.html', context)
