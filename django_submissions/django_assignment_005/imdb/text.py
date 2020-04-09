from imdb.utils import *


populate_database(
    actors_list=[
        {
            'actor_id':1,
            'name':'Actor-1',
            'date_of_birth':'1990-04-17',
            'gender':'MALE'
        },
        {
            'actor_id':2,
            'name':'Actor-2',
            'date_of_birth':'2000-03-21',
            'gender':'FEMALE'
        },
        {
            'actor_id':3,
            'name':'Actor-3',
            'date_of_birth':'1995-01-1',
            'gender':'FEMALE'
        },
        {
            'actor_id':4,
            'name':'Actor-4',
            'date_of_birth':'1975-10-7',
            'gender':'MALE'
        },
        {
            'actor_id':5,
            'name':'Actor-5',
            'date_of_birth':'1930-02-27',
            'gender':'MALE'
        },
    ]
)


populate_database(
    directors_list=[
        'Director-1','Director-2','Director-3','Director-4','Director-5'
    ]
)



populate_database(   
    movies_list= [
            {
                "movie_id": "1",
                "name": "Movie-1",
                "actors": [
                    {
                        "actor_id": 1,
                        "role": "hero",
                        "is_debut_movie": False,
                        "remuneration":20
                    }
                ],
                "box_office_collection_in_crores": "12.3",
                "release_date": "1999-3-3",
                "director_name": "Director-1",
                'genre':'comedy',
                'rating':2.0
            },
            {
                "movie_id": "2",
                "name": "Movie-2",
                "actors": [
                    {
                        "actor_id": 1,
                        "role": "hero",
                        "is_debut_movie": False,
                        "remuneration":10
                    },
                    {
                        "actor_id": 2,
                        "role": "heroine",
                        "is_debut_movie": False,
                        "remuneration":5
                    },
                    {
                        "actor_id": 3,
                        "role": "Vilan",
                        "is_debut_movie": False,
                        "remuneration":2
                    },
                    {
                        "actor_id": 4,
                        "role": "side-actor",
                        "is_debut_movie": False,
                        "remuneration":1
                    }
                ],
                "box_office_collection_in_crores": "20",
                "release_date": "2004-4-23",
                "director_name": "Director-2",
                'genre':'horror',
                'rating':3.0
            },
            {
                "movie_id": "3",
                "name": "Movie-3",
                "actors": [
                    {
                        "actor_id": 3,
                        "role": "hero",
                        "is_debut_movie": False,
                        "remuneration":7
                    },
                    {
                        "actor_id": 1,
                        "role": "heroine",
                        "is_debut_movie": False,
                        "remuneration":4
                    },
                    {
                        "actor_id": 2,
                        "role": "Vilan",
                        "is_debut_movie": False,
                        "remuneration":1
                    },
                    {
                        "actor_id": 4,
                        "role": "side-actor",
                        "is_debut_movie": False,
                        "remuneration":1
                    }
                ],
                "box_office_collection_in_crores": "40",
                "release_date": "2007-12-17",
                "director_name": "Director-3",
                'genre':'action_adventure',
                'rating':2.5
            },
            {
                "movie_id": "4",
                "name": "Movie-4",
                "actors": [
                    {
                        "actor_id": 5,
                        "role": "hero",
                        "is_debut_movie": False,
                        "remuneration":20
                    },
                    {
                        "actor_id": 2,
                        "role": "heroine",
                        "is_debut_movie": False,
                        "remuneration":7
                    },
                    {
                        "actor_id": 1,
                        "role": "Vilan",
                        "is_debut_movie": False,
                        "remuneration":4
                    },
                    {
                        "actor_id": 4,
                        "role": "side-actor",
                        "is_debut_movie": False,
                        "remuneration":1
                    }
                ],
                "box_office_collection_in_crores": "10",
                "release_date": "2010-2-13",
                "director_name": "Director-4",
                'genre':'science_fiction',
                'rating':1.0
            },
            {
                "movie_id": "5",
                "name": "Movie-5",
                "actors": [
                    {
                        "actor_id": 3,
                        "role": "hero",
                        "is_debut_movie": False,
                        "remuneration":12
                    },
                    {
                        "actor_id": 2,
                        "role": "heroine",
                        "is_debut_movie": False,
                        "remuneration":6
                    },
                    {
                        "actor_id": 1,
                        "role": "Vilan",
                        "is_debut_movie": False,
                        "remuneration":4
                    },
                    {
                        "actor_id": 5,
                        "role": "side-actor",
                        "is_debut_movie": False,
                        "remuneration":1
                    }
                ],
                "box_office_collection_in_crores": "5",
                "release_date": "1999-6-15",
                "director_name": "Director-5",
                'genre':'comedy',
                'rating':2.7
            }
        ]
    )


populate_database(
    movie_rating_list=[
        {
            "movie_id":"1",
            "rating_one_count":4000,
            "rating_two_count":2000,
            "rating_three_count":1000,
            "rating_four_count":500,
            "rating_five_count":100
        },
        {
            "movie_id":"2",
            "rating_one_count":10000,
            "rating_two_count":4000,
            "rating_three_count":2000,
            "rating_four_count":1000,
            "rating_five_count":500
        },
        {
            "movie_id":"3",
            "rating_one_count":8000,
            "rating_two_count":2000,
            "rating_three_count":500,
            "rating_four_count":500,
            "rating_five_count":100
        },
        {
            "movie_id":"4",
            "rating_one_count":7000,
            "rating_two_count":4000,
            "rating_three_count":2000,
            "rating_four_count":1000,
            "rating_five_count":100
        },
        {
            "movie_id":"5",
            "rating_one_count":5000,
            "rating_two_count":4000,
            "rating_three_count":3000,
            "rating_four_count":2000,
            "rating_five_count":1000
        }
        ]
    )

def get_female_cast_details_from_movies_having_more_than_five_female_cast():
    movie_objs=Movie.objects.annotate(
                num_female_actors=Count('actors',filter=Q(actors__gender='FEMALE'))
                ).filter(num_female_actors__gte=5)
    return return(movie_objs,female=1)

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
        'num_female_actors'
        )
    female_movies_list=[]    
    if(female==1):
        for mov in all_movies:
            if(mov['actors__gender']=='FEMALE' and mov['num_female_actors']>=5):
                female_movies_list.append(mov)
        update_of_all_movies=female_movies_list
    else:
        update_of_all_movies=all_movies
    movies_dict = {}
    for each_movie in update_of_all_movies:
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