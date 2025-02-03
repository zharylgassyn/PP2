# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1.
def is_highly_rated(movie):
    return movie["imdb"] > 5.5
print(is_highly_rated(movies[0]))

# 2.

def highly_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]
filtered_movies = highly_rated_movies(movies)
print(filtered_movies)

# 3.

def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]

category_name = "Romance"
filtered_movies = movies_by_category(movies, category_name)
print(filtered_movies)


#4. 
def average_imdb_score(movies):
    if not movies:  
        return 0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)
print(average_imdb_score(movies)) 
#5.
def average_imdb_by_category(movies, category):
    filtered_movies = []
    
    for movie in movies:
        if movie["category"].lower() == category.lower():
            filtered_movies.append(movie)

    if len(filtered_movies) == 0:
        return 0
    
    total_score = 0
    for movie in filtered_movies:
        total_score += movie["imdb"]
    
    return total_score / len(filtered_movies)

category_name = "Romance"
print(average_imdb_by_category(movies, category_name))  