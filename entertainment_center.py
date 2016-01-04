import media
import fresh_tomatoes

rang_de_basanti = media.Movie("Rang De Basanti",
                              "The story of six young Indians who assist an English Woman to film a documentary on the extremist freedom fighters from their past, and the events that lead them to relive the long forgotten saga of freedom.",
                              "https://upload.wikimedia.org/wikipedia/en/5/5f/RDB_poster.jpg",
                              "https://www.youtube.com/watch?v=9U5gGXvJxO8")

dil_chahta_hain = media.Movie("Dil Chahta Hai",
                              "Three inseparable childhood friends are just out of college. Nothing comes between them - until they each fall in love, and their wildly different approaches to relationships creates tension. ",
                              "https://upload.wikimedia.org/wikipedia/en/d/db/Dil_Chahta_Hai.jpg",
                              "https://www.youtube.com/watch?v=m13b25V0B10")

swades = media.Movie("Swades",
                     "A successful Indian scientist returns to an Indian village to take his nanny to America with him and in the process rediscovers his roots.",
                     "https://upload.wikimedia.org/wikipedia/en/5/5f/Swades_movie_poster.png",
                     "https://www.youtube.com/watch?v=y95DpoSP7i0")

movies = [rang_de_basanti, dil_chahta_hain, swades]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#media.Movie.__name__ = "MovieWebsite.media.Movie"
#print(media.Movie.__name__)
#media.Movie.__module__ = "dynamically_defined_function"
#print(media.Movie.__module__)
