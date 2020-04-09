from imdb.utils import *
'''
populate_database(
    actors_list=[
        {
            'actor_id':1,
            'name':'Actor-1',
            'date_of_birth':'2020-03-17',
            'gender':'Male'
        },
        {
            'actor_id':2,
            'name':'Actor-2',
            'date_of_birth':'2020-03-17',
            'gender':'Female'
        },
        {
            'actor_id':3,
            'name':'Actor-3',
            'date_of_birth':'2020-03-17',
            'gender':'Female'
        },
        {
            'actor_id':4,
            'name':'Actor-5',
            'date_of_birth':'2020-03-17',
            'gender':'Male'
        },
        {
            'actor_id':5,
            'name':'Actor-5',
            'date_of_birth':'2020-03-17',
            'gender':'Male'
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
                "release_date": "2020-3-3",
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
                "release_date": "2020-3-3",
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
                "release_date": "2020-3-3",
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
                "release_date": "2020-3-3",
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
                "release_date": "2020-3-3",
                "director_name": "Director-5",
                'genre':'comedy',
                'rating':2.7
            }
        ]
    )
'''

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