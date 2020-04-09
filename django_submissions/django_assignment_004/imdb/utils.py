from .models import *

def populate_database(
        actors_list=[], movies_list=[], directors_list=[], movie_rating_list=[]):
    
    for actor in actors_list:
        Actor.objects.create(actor_id=actor['actor_id'],
                            name=actor['name'],
                            gender=actor['gender']
                            )
    
    for director in directors_list:
        Director.objects.create(name=director)
    
    for movie in movies_list:
        movie_obj=Movie.objects.create(movie_id=movie['movie_id'],
                                        name=movie['name'],    
                                        box_office_collection_in_crores=movie['box_office_collection_in_crores'],
                                        release_date=movie['release_date'],
                                        director=Director.objects.get(name=movie['director_name'])
                                        )
        cast_list=movie['actors']
        for cast_item in cast_list:
                Cast.objects.create(
                    actor=Actor.objects.get(actor_id=cast_item['actor_id']),
                    movie=movie_obj,
                    role=cast_item['role'],
                    is_debut_movie=cast_item['is_debut_movie']
                    )
                                        
    for movie_rating_obj in movie_rating_list:
        Rating.objects.create(
            movie=Movie.objects.get(movie_id=movie_rating_obj['movie_id']),
            rating_one_count=movie_rating_obj['rating_one_count'],
            rating_two_count=movie_rating_obj['rating_two_count'],
            rating_three_count=movie_rating_obj['rating_three_count'],
            rating_four_count=movie_rating_obj['rating_four_count'],
            rating_five_count=movie_rating_obj['rating_five_count'],
            )

from django.db.models import Sum,Avg,Count,Min,Max,FloatField,Q

#Task-1
def get_average_box_office_collections():
    Avg_box_office_collection = Movie.objects.aggregate(
        Average_collection=Avg('box_office_collection_in_crores',output_field=FloatField())
    )
    avg=Avg_box_office_collection['Average_collection']
    if(avg==None):
        return 0
    else:
        return round(avg,3)

#Task-2    
def get_movies_with_distinct_actors_count():
    return Movie.objects.annotate(actors_count=Count('actors',distinct=True))

#Task-3
def get_male_and_female_actors_count_for_each_movie():
    movie_objs=Movie.objects.annotate(
        male_actors_count=Count('actors',distinct=True,filter=Q(actors__gender='MALE')),
        female_actors_count=Count('actors',distinct=True,filter=Q(actors__gender='FEMALE'))
    )
    return movie_objs

#Task-4
def get_roles_count_for_each_movie():
    movie_objs=Movie.objects.annotate(
        roles_count=Count('cast__role',distinct=True)
    )
    return movie_objs

#Task-5
def get_role_frequency():
    role_and_roles_count=Cast.objects.values('role').annotate(roles_count=Count('actor',distinct=True))
    role_frequency={}
    for obj in role_and_roles_count:
        role_frequency[obj['role']]=obj['roles_count']
    return role_frequency

#Task-6
def get_role_frequency_in_order():
    queryset=Cast.objects.values('role').annotate(
        roles_count=Count('role')
    ).values_list('role','roles_count').order_by('-movie__release_date')  
    return list(queryset)

#Task-7
def get_no_of_movies_and_distinct_roles_for_each_actor():
    actor_objs=Actor.objects.annotate(
        movies_count=Count('movie',distinct=True),
        roles_count=Count('cast__role',distinct=True)
    )
    return list(actor_objs)

#Task-8
def get_movies_with_atleast_forty_actors():
    movie_objs=Movie.objects.annotate(actors_count=Count('actors',distinct=True)).filter(actors_count__gte=40)
    return list(movie_objs)

#Task-9
def get_average_no_of_actors_for_all_movies():
    avg_actors_dict=Movie.objects.annotate(num_actors=Count('actors')).aggregate(avg_actors=Avg('num_actors'))
    avg=avg_actors_dict['avg_actors']
    if(avg==None):
        return 0
    else:
        return round(avg,3)
        