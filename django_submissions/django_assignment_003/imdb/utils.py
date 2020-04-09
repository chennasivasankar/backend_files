from .models import *
from datetime import datetime,date,time
import json
from django.db.models import Q

def get_average_rating_of_movie(movie_obj):
    try:
        movie_rating=Rating.objects.get(movie=movie_obj)
        return (movie_rating.rating_one_count+movie_rating.rating_two_count*2+
                movie_rating.rating_three_count*3+movie_rating.rating_four_count*4+
                movie_rating.rating_five_count*5)/(movie_rating.rating_one_count+movie_rating.rating_two_count+
                movie_rating.rating_three_count+movie_rating.rating_four_count+
                movie_rating.rating_five_count)
    except:
        return 0

def total_number_of_rating_of_movie(movie_obj):
    try:
        movie_rating_obj=Rating.objects.get(movie=movie_obj)
        return (movie_rating_obj.rating_one_count+movie_rating_obj.rating_two_count+
                movie_rating_obj.rating_three_count+movie_rating_obj.rating_four_count+
                movie_rating_obj.rating_five_count)
    except:
        return 0
   

def get_movies_by_given_movie_objs(movie_objs):
    all_movies_inf=[]
    for movie_obj in movie_objs:
        movie_inf={}
        movie_inf['movie_id']=movie_obj.movie_id
        movie_inf['name']=movie_obj.name
        movie_inf['box_office_collection_in_crores']=movie_obj.box_office_collection_in_crores
        movie_inf['release_date']=movie_obj.release_date.strftime('%Y-%m-%d')
        movie_inf['director_name']=movie_obj.director.name
        movie_inf['average_rating']=get_average_rating_of_movie(movie_obj)
        movie_inf['total_number_of_ratings']=total_number_of_rating_of_movie(movie_obj)
        cast=[]
        for cast_item in Cast.objects.filter(movie=movie_obj):
            cast_info = {}
            cast_info['role']=cast_item.role
            cast_info['is_debut_movie']=cast_item.is_debut_movie
            actor_info = {}
            actor_info['name']=cast_item.actor.name
            actor_info['actor_id']=cast_item.actor.actor_id
            cast_info['actor']=actor_info
            cast.append(cast_info)
        movie_inf['cast']=cast
        all_movies_inf.append(movie_inf)
    json_file_of_all_movies_inf=json.dumps(all_movies_inf)        
    return all_movies_inf

#Task-1
def get_movies_by_given_movie_names(movie_names):
    movie_objs=Movie.objects.filter(name__in=movie_names)
    movies_info=get_movies_by_given_movie_objs(movie_objs)
    return movies_info

#Task-2        
def get_movies_released_in_summer_in_given_years():
    movie_objs = Movie.objects.filter(
        release_date__year__gt=2005,
        release_date__year__lt=2010,
        release_date__month__in=[5,6,7]
    )
    return get_movies_by_given_movie_objs(movie_objs)

#Task-3
def get_movie_names_with_actor_name_ending_with_smith():
    movie_names=Movie.objects.filter(
        actors__name__iendswith='smith'
    ).distinct().values_list('name',flat=True)
    #movie_names=[movie.name for movie in movie_objs]
    return list(movie_names)

#Task-4
def get_movie_names_with_ratings_in_given_range():
    movie_names=Movie.objects.filter(
        rating__rating_five_count__gte=1000,
        rating__rating_five_count__lte=3000
    ).values_list('name',flat=True).distinct()
            
    return list(movie_names)

#Task-5
def get_movie_names_with_ratings_above_given_minimum():
    movie_names=Movie.objects.filter(
        Q(rating__rating_five_count__gte=500)|
        Q(rating__rating_four_count__gte=1000)|
        Q(rating__rating_three_count__gte=2000)|
        Q(rating__rating_two_count__gte=4000)|
        Q(rating__rating_one_count__gte=8000),
        release_date__year__gt=2000
    ).values_list('name',flat=True).distinct()
    return list(movie_names)
    

#Task-6
def get_movie_directors_in_given_year():
    director_names=Director.objects.filter(
        movie__release_date__year=2000
    ).distinct().values_list('name',flat=True)
    return list(director_names) 

#Task-7
def get_actor_names_debuted_in_21st_century():
    actors_name=Cast.objects.filter(
        movie__release_date__year__gt=2000,
        is_debut_movie=True,
        movie__release_date__year__lte=2100
    ).values_list('actor__name',flat=True).distinct()
    return list(actors_name)

#Task-8
def get_director_names_containing_big_as_well_as_movie_in_may():
    director_names=Director.objects.filter(
        Q(movie__name__contains='big')
    ).filter(
        Q(movie__release_date__month=5)        
    ).values_list('name',flat=True).distinct()
    return list(director_names)

#Task-9
def get_director_names_containing_big_and_movie_in_may():
    director_names=Movie.objects.filter(
        release_date__month=5,name__contains='big'
    ).values_list('director__name',flat=True).distinct()
    return list(director_names)

#Task-10
def reset_ratings_for_movies_in_this_year():
    Rating.objects.filter(
        movie__release_date__year=2000
    ).update(
        rating_five_count=0,
        rating_one_count=0,
        rating_two_count=0,
        rating_three_count=0,
        rating_four_count=0
    )    

