import fresh_tomatoes
import media

toy_story=media.Movie("Toy Story",
                      "A story of a boy and his toys which comes to life",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar=media.Movie("Avatar",
                   "A marine on alien planet",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock=media.Movie("School of rock",
                           "Using rock music to learn",
                           "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                           "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille=media.Movie("ratatouille",
                        "A rat is a chef in Paris",
                        "https://en.wikipedia.org/wiki/Ratatouille_(film)#/media/File:RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=1yKqLNnxGZw")


midnight_in_paris=media.Movie("Midnight in paris",
                              "Going back in time to meet authors",
                              "https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg",
                              "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games=media.Movie("Hunger games",
                         "A really real reality show",
                         "https://en.wikipedia.org/wiki/The_Hunger_Games_(film)#/media/File:HungerGamesPoster.jpg",
                         "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies=[toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]
fresh_tomatoes.open_movies_page(movies)

