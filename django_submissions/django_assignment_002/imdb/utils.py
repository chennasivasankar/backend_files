from .models import *

#Task 2
def populate_database(
        actors_list=[], movies_list=[], directors_list=[], movie_rating_list=[]):
    
    for actor in actors_list:
        Actor.objects.create(actor_id=actor['actor_id'],name=actor['name'])
    
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



#Task 3
def get_no_of_distinct_movies_actor_acted(actor_id):
    return Movie.objects.all().filter(actors__actor_id=actor_id).distinct().count()
    
#Task 4    
def get_movies_directed_by_director(director_obj):
    return Movie.objects.filter(director=director_obj)

#Task 5
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
        
#Task 6
def delete_movie_rating(movie_obj):
    Rating.objects.get(movie=movie_obj).delete()

#Task 7
def get_all_actor_objects_acted_in_given_movies(movie_objs):
    return Actor.objects.filter(movie__in=movie_objs).distinct()
    
    
#Task 8
def update_director_for_given_movie(movie_obj, director_obj):
    movie_obj.director=director_obj
    movie_obj.save()

#Task 9
def get_distinct_movies_acted_by_actor_whose_name_contains_john():
    return Movie.objects.filter(actors__name__contains='john').distinct()

#Task 10
def remove_all_actors_from_given_movie(movie_obj):
    #Cast.objects.get(movie=movie_obj).delete()
    movie_obj.actors.clear()

#Task 11
def get_all_rating_objects_for_given_movies(movie_objs):
    return Rating.objects.filter(movie__in=movie_objs)
    
def get_all_distinct_actors_for_given_movie(movie_obj):
    return movie_obj.actors.distinct()