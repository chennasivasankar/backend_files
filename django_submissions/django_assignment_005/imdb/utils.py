from .models import *
from django.db import *
from django.db.models import *
from collections import defaultdict 

def profile():
    def decorator(func):
        def handler(*args, **kwargs):
            import line_profiler
            profiler = line_profiler.LineProfiler()
            profiler.enable_by_count()
            profiler.add_function(func)
            result = func(*args, **kwargs)
            profiler.print_stats()
            return result

        handler.__doc__ = func.__doc__
        return handler

    return decorator

def total_number_of_rating_of_movie(mov):
    try:
        movie_rating_obj=mov.rating
        return (movie_rating_obj.rating_one_count+movie_rating_obj.rating_two_count+
                movie_rating_obj.rating_three_count+movie_rating_obj.rating_four_count+
                movie_rating_obj.rating_five_count)
    except:
        return 0

def get_average_rating_of_movie(mov):
    try:
        movie_rating=mov.rating
        return (movie_rating.rating_one_count+movie_rating.rating_two_count*2+
                movie_rating.rating_three_count*3+movie_rating.rating_four_count*4+
                movie_rating.rating_five_count*5)/(movie_rating.rating_one_count+movie_rating.rating_two_count+
                movie_rating.rating_three_count+movie_rating.rating_four_count+
                movie_rating.rating_five_count)
    except:
        return 0

# def get_movies_by_given_movie_objs(movie_objs,female=0,male=0):
#     cast_list=Cast.objects.filter(
#             movie__in=movie_objs
#         ).select_related(
#                 'actor',
#                 'movie__director',
#                 'movie__rating'
#             )
#     from collections import defaultdict
#     movie_cast_dict=defaultdict(list)
#     for cast_item in cast_list:
#         movie_cast_dict[cast_item.movie].append(cast_item)
    
#     all_movies_details=[]
#     for movie,casts in movie_cast_dict.items():
#         cast_details=[]
#         for cast in casts:
#             actor_info={
#                 'name':cast.actor.name,
#                 'actor_id':cast.actor.actor_id
#             }
            
#             cast_info={
#                 'actor':actor_info,
#                 'role':cast.role,
#                 'is_debut_movie':cast.is_debut_movie
#             }
#             cast_details.append(cast_info)
#         movie_info={
#             'movie_id':movie.movie_id,
#             'name':movie.name,
#             'cast':cast_details,
#             'box_office_collection_in_crores':movie.box_office_collection_in_crores,
#             'release_date':str(movie.release_date),
#             'director_name':movie.director.name,
#             'average_rating':get_average_rating_of_movie(movie),
#             'total_number_of_ratings':total_number_of_rating_of_movie(movie)
#         }
#         all_movies_details.append(movie_info)
#     return all_movies_details

def get_movies_by_given_movie_objs(movie_objs=0,cast_objs=0):
    if(cast_objs==0):
        cast_list=Cast.objects.filter(
                movie__in=movie_objs
            ).select_related(
                    'actor',
                    'movie__director',
                    'movie__rating'
                )
    if(movie_objs==0):
        cast_list=cast_objs
        
    from collections import defaultdict
    movie_cast_dict=defaultdict(list)
    for cast_item in cast_list:
        movie_cast_dict[cast_item.movie].append(cast_item)
    
    all_movies_details=[]
    for movie,casts in movie_cast_dict.items():
        cast_details=[]
        for cast in casts:
            actor_info={
                'name':cast.actor.name,
                'actor_id':cast.actor.actor_id
            }
            
            cast_info={
                'actor':actor_info,
                'role':cast.role,
                'is_debut_movie':cast.is_debut_movie
            }
            cast_details.append(cast_info)
        movie_info={
            'movie_id':movie.movie_id,
            'name':movie.name,
            'cast':cast_details,
            'box_office_collection_in_crores':movie.box_office_collection_in_crores,
            'release_date':str(movie.release_date),
            'director_name':movie.director.name,
            'average_rating':get_average_rating_of_movie(movie),
            'total_number_of_ratings':total_number_of_rating_of_movie(movie)
        }
        all_movies_details.append(movie_info)
    return all_movies_details

    
def get_actor_details_by_actor_objs(actor_objs):
    actors_details_list=[]
    for actor_obj in actor_objs:
        actor_mov_list=[]
        for actor_mov in actor_obj.movie_set.all():
            cast_detail=[]
            for cast_item in actor_mov.cast_set.all():
                if(cast_item.actor.actor_id==actor_obj.actor_id):
                    cast_info={
                        "role":cast_item.role,
                        "is_debut_movie":cast_item.is_debut_movie
                    }
                    cast_detail.append(cast_info)
            actor_mov_detail={
                "movie_id":actor_mov.movie_id,
                "name":actor_mov.name,
                "cast":cast_detail,
                "box_office_collection_in_crores":actor_mov.box_office_collection_in_crores,
                "release_date":str(actor_mov.release_date),
                "director_name":actor_mov.director.name,
                "average_rating":get_average_rating_of_movie(actor_mov),
                "total_number_of_ratings":total_number_of_rating_of_movie(actor_mov)
            }
            actor_mov_list.append(actor_mov_detail)
        actor_info={
            "name":actor_obj.name,
            "actor_id":actor_obj.actor_id,
            "movies":actor_mov_list
        }
        actors_details_list.append(actor_info)
    return(actors_details_list)


#Task-1-done

def populate_database(actors_list=[], movies_list=[], directors_list=[], movie_rating_list=[]):

    loaded_actors_list=[]
    for actor in actors_list:
        actor_model=Actor(
            actor_id=actor['actor_id'],
            name=actor['name'],
            gender=actor['gender']
            )
        loaded_actors_list.append(actor_model)    
    Actor.objects.bulk_create(loaded_actors_list)
    
    
    loaded_directors_list=[]
    for director in directors_list:
        director_model=Director(
                name=director
            )
        loaded_directors_list.append(director_model)
    Director.objects.bulk_create(loaded_directors_list)
    
    
    loaded_movie_list=[]
    loaded_cast_list=[]
    if(movies_list):
        director_name_id_dict={}
        director_objs=Director.objects.all()
        for director_obj in director_objs:
            director_name_id_dict[director_obj.name]=director_obj.id

    for movie in movies_list:
        movie_obj=Movie(
            movie_id=movie['movie_id'],
            name=movie['name'],    
            box_office_collection_in_crores=movie['box_office_collection_in_crores'],
            release_date=movie['release_date'],
            director_id=director_name_id_dict[movie['director_name']]
            )
        loaded_movie_list.append(movie_obj)
        cast_list=movie['actors']
        for cast_item in cast_list:
            cast_obj=Cast(
                actor_id=cast_item['actor_id'],
                    movie_id=movie['movie_id'],
                    role=cast_item['role'],
                    is_debut_movie=cast_item['is_debut_movie']
                )
            loaded_cast_list.append(cast_obj)
    Movie.objects.bulk_create(loaded_movie_list)
    Cast.objects.bulk_create(loaded_cast_list)
    
    loaded_movie_rating_list=[]
    for movie_rating_obj in movie_rating_list:
        rating_model=Rating(
            movie_id=movie_rating_obj['movie_id'],
            rating_one_count=movie_rating_obj['rating_one_count'],
            rating_two_count=movie_rating_obj['rating_two_count'],
            rating_three_count=movie_rating_obj['rating_three_count'],
            rating_four_count=movie_rating_obj['rating_four_count'],
            rating_five_count=movie_rating_obj['rating_five_count'],
            )
        loaded_movie_rating_list.append(rating_model)
    Rating.objects.bulk_create(loaded_movie_rating_list)

from django.db.models import Sum,Avg,Count,Min,Max,FloatField,Q


#Task-2-done

def remove_all_actors_from_given_movie(movie_object):
    movie_object.actors.clear()


#Task-3-done

def get_all_rating_objects_for_given_movies(movie_objs):
    return list(Rating.objects.filter(movie_id__in=movie_objs))
    
#Task-4

def get_movies_by_given_movie_names(movie_names):
    movie_objs=Movie.objects.filter(name__in=movie_names)
    movies_info=get_movies_by_given_movie_objs(movie_objs=movie_objs)
    return movies_info


#Task-5-done

def get_all_actor_objects_acted_in_given_movies(movie_objs):
    return list(Actor.objects.filter(
                movie__in=movie_objs
            ).distinct())
            
#Task-6-done

# def get_female_cast_details_from_movies_having_more_than_five_female_cast():
#     movie_cast_objs=defaultdict(list)
#     cast_objs=Cast.objects.select_related('actor','movie__rating','movie__director')
    
#     for cast_obj in cast_objs:
#         if(cast_obj.actor.gender=='FEMALE'):
#             movie_cast_objs[cast_obj.movie].append(cast_obj)
   
#     all_movies_details=[]
#     for movie,cast_objs_list in movie_cast_objs.items():
#         cast_details=[]
#         female_count=0
#         for cast_item in cast_objs_list:
#             female_count+=1
#             actor_info={
#                 "name":cast_item.actor.name,
#                 "actor_id":cast_item.actor.actor_id
#             }
#             cast_info={
#                 "actor":actor_info,
#                 "role":cast_item.role,
#                 "is_debut_movie":cast_item.is_debut_movie
#             }
#             cast_details.append(cast_info)
#         movie_info={
#             "movie_id":movie.movie_id,
#             "name":movie.name,
#             "cast":cast_details,
#             "box_office_collection_in_crores":movie.box_office_collection_in_crores,
#             "release_date":str(movie.release_date),
#             "director_name":movie.director.name,
#             "average_rating":get_average_rating_of_movie(movie),
#             "total_number_of_ratings":total_number_of_rating_of_movie(movie)
#         }
#         if(female_count>5):
#             all_movies_details.append(movie_info)
#     return all_movies_details
    
    
#Task-7-done

def get_actor_movies_released_in_year_greater_than_or_equal_to_2000():
    actor_objs=Actor.objects.filter(
            movie__release_date__year__gte=2000
        ).prefetch_related(
            Prefetch(
                'movie_set',
                 queryset=Movie.objects.filter(
                        release_date__year__gte =2000
                    ).select_related(
                        'director','rating'
                    ).prefetch_related(
                        Prefetch(
                            'cast_set',
                            queryset=Cast.objects.select_related('actor')
                            )
                        )
                )
            ).distinct()
    return get_actor_details_by_actor_objs(actor_objs)


#Task-8-done

def reset_ratings_for_movies_in_given_year(year):
    Rating.objects.filter(
        movie__release_date__year=year
    ).update(
        rating_five_count=0,
        rating_one_count=0,
        rating_two_count=0,
        rating_three_count=0,
        rating_four_count=0
    )    
    
    
#changed_Task-6

def get_female_cast_details_from_movies_having_more_than_five_female_cast():
    cast_objs = Cast.objects.filter(
            actor__gender='FEMALE'
        ).filter(
                movie__in=Movie.objects.annotate(
                    num_female_actors=Count('actors',filter=Q(actors__gender='FEMALE'))
                    ).filter(
                            num_female_actors__gt=5
                        )
            ).select_related(
                'actor',
                'movie__director',
                'movie__rating'
                )
    return get_movies_by_given_movie_objs(cast_objs=cast_objs)

#copied-task
def returning_movie_json1(movies_list,female=0):
    all_movies = movies_list.values('movie_id',
        'name',
        'release_date',
        'box_office_collection_in_crores',
        'director__name',
        'actors__name',
        'actors__actor_id',
        'actors__gender',
        'cast__role',
        'cast__is_debut_movie',
        'rating__rating_one_count',
        'rating__rating_two_count',
        'rating__rating_three_count',
        'rating__rating_four_count',
        'rating__rating_five_count',
        )
    movies_dict = {}
    for each_movie in all_movies:
        #print(movies_dict.keys())
        if each_movie['movie_id'] not in movies_dict.keys():
            movies_dict[each_movie['movie_id']] = {}
            movies_dict[each_movie['movie_id']]['movie_id'] = each_movie['movie_id']
            movies_dict[each_movie['movie_id']]['name'] = each_movie['name']
            movie_cast = []
            cast_dict = {}
            actor_dict = {}
            actor_dict['name'] = each_movie['actors__name']
            actor_dict['actor_id'] = each_movie['actors__actor_id']
            cast_dict['actor'] = actor_dict
            cast_dict['role'] = each_movie['cast__role']
            cast_dict['is_debut_movie'] = each_movie['cast__is_debut_movie']
            movie_cast.append(cast_dict)
            movies_dict[each_movie['movie_id']]['cast'] = movie_cast
            movies_dict[each_movie['movie_id']]['box_office_collection_in_crores'] = each_movie['box_office_collection_in_crores']
            movies_dict[each_movie['movie_id']]['release_date'] = str(each_movie['release_date'])
            movies_dict[each_movie['movie_id']]['director_name'] = each_movie['director__name']
            if each_movie['rating__rating_five_count'] == None:
                movies_dict[each_movie['movie_id']]['average_rating'] = 0
                movies_dict[each_movie['movie_id']]['total_number_of_ratings'] = 0
            else:
                try:
                    five = each_movie['rating__rating_five_count']
                    four = each_movie['rating__rating_four_count']
                    three = each_movie['rating__rating_three_count']
                    two = each_movie['rating__rating_two_count']
                    one = each_movie['rating__rating_one_count']
                    movies_dict[each_movie['movie_id']]['average_rating'] = (one*1+two*2+three*3+four*4+five*5)/(one+two+three+four+five)
                    movies_dict[each_movie['movie_id']]['total_number_of_ratings'] = one+two+three+four+five
                except:
                    movies_dict[each_movie['movie_id']]['average_rating'] = 0
                    movies_dict[each_movie['movie_id']]['total_number_of_ratings'] = 0
        else:
            cast_dict = {}
            actor_dict = {}
            actor_dict['name'] = each_movie['actors__name']
            actor_dict['actor_id'] = each_movie['actors__actor_id']
            cast_dict['actor'] = actor_dict
            cast_dict['role'] = each_movie['cast__role']
            cast_dict['is_debut_movie'] = each_movie['cast__is_debut_movie']
            movies_dict[each_movie['movie_id']]['cast'].append(cast_dict)
    result_list = []
    for each in movies_dict:
        result_list.append(movies_dict[each])
    return result_list