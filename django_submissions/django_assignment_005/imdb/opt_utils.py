from .models import *
from django.db.models import *
from django.db import *

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

# def get_female_cast_details_from_movies_having_more_than_five_female_cast():
#     movie_objs=Movie.objects.annotate(
#                 num_female_actors=Count('actors',filter=Q(actors__gender='FEMALE'))
#                 ).filter(num_female_actors__gte=2)
#     print(movie_objs)
#     return returning_movie_json1(movie_objs,female=1)

def returning_movie_json1(movies_list,female=0):
    print('sa')
    print(movies_list.values())
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
    print(all_movies)
    movies_dict = {}
    for each_movie in all_movies:
        #print(movies_dict.keys())
        if each_movie['movie_id'] not in movies_dict.keys():
            movies_dict[each_movie['movie_id']] = {}
            movies_dict[each_movie['movie_id']]['movie_id'] = each_movie['movie_id']
            movies_dict[each_movie['movie_id']]['name'] = each_movie['name']
            movie_cast = []
            cast_dict = {}
            if(female==1 and each_movie['actors__gender']=='MALE'):
                movie_cast.append(cast_dict)
                continue
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
            if(female==1 and each_movie['actors__gender']=='MALE'):
                continue
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
    
    
# from collections import defaultdict 
# def get_female_cast_details_from_movies_having_more_than_five_female_cast():
#     movie_cast_objs=defaultdict(list)
#     cast_obs=Cast.objects.select_related('actor','movie__rating','movie__director')
#     for cast_obj in Cast.objects.all():
#         movie_cast_objs[cast_obj.movie].append(cast_obj)
    
#     all_movies_details=[]
#     for movie,cast_objs_list in movie_cast_objs.items():
#         cast_details=[]
#         female_count=0
#         for cast_item in cast_objs_list:
#             if(cast_item.actor.gender=='MALE'):
#                 continue
#             else:
#                 female_count+=1
#                 actor_info={
#                     "name":cast_item.actor.name,
#                     "actor_id":cast_item.actor.actor_id
#                 }
#                 cast_info={
#                     "actor":actor_info,
#                     "role":cast_item.role,
#                     "is_debut_movie":cast_item.is_debut_movie
#                 }
#                 cast_details.append(cast_info)
#             movie_info={
#                 "movie_id":movie.movie_id,
#                 "name":movie.name,
#                 "cast":cast_details,
#                 "box_office_collection_in_crores":movie.box_office_collection_in_crores,
#                 "director_name":movie.director.name,
#                 "average_rating":get_average_rating_of_movie(movie),
#                 "total_number_of_ratings":total_number_of_rating_of_movie(movie)
#             }
#         if(female_count>5):
#             all_movies_details.append(movie_info)
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
            'movie_id':movie,
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


def get_female_cast_details_from_movies_having_more_than_five_female_cast():
    cast_objs = Cast.objects.filter(
            actor__gender='FEMALE'
        ).filter(
                movie__in=Movie.objects.annotate(
                    num_female_actors=Count('actors',filter=Q(actors__gender='FEMALE'))
                    ).filter(
                            num_female_actors__gt=5
                        )
            )
    return get_movies_by_given_movie_objs(cast_objs=cast_objs)