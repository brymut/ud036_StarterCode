import media
import fresh_tomatoes

# creating movie object instances and adding to list
christopher_robin = media.Movie("Christopher Robin",
                                "The little boy from the Winnie-the-Pooh "
                                "stories, is now all grown up and has lost "
                                "all sense of imagination.",
                                "https://upload.wikimedia.org/wikipedia/en/a"
                                "/a9/Christopher_Robin_poster.png",
                                "https://www.youtube.com/watch?v=mecs05sjbRU")
bohemian_rhapsody = media.Movie("Bohemian Rhapsody",
                                "Bohemian Rhapsody is an upcoming "
                                "biographical musical film about the British "
                                "rock "
                                "band Queen",
                                "https://upload.wikimedia.org/wikipedia/en/2"
                                "/2e/Bohemian_Rhapsody_poster.png",
                                "https://www.youtube.com/watch?v=6S9c5nnDd_s")
red_sparrow = media.Movie("Red Sparrow",
                          "Ballerina Dominika Egorova is recruited to "
                          "'Sparrow School,' a Russian intelligence "
                          "service where she is forced to use her body as a "
                          "weapon.",
                          "https://upload.wikimedia.org/wikipedia/en/5/5a"
                          "/Red_Sparrow.png",
                          "https://www.youtube.com/watch?v=tv4H4tN4yBA")
the_darkest_minds = media.Movie("The darkest minds",
                                "After a plague kills nearly all of "
                                "America's children, the ones left are given "
                                "special abilities.",
                                "https://upload.wikimedia.org/wikipedia/en/7"
                                "/7f/The_Darkest_Minds_teaser_poster.jpg",
                                "https://www.youtube.com/watch?v=tN8o_E_f9FQ")

movies = [christopher_robin, bohemian_rhapsody, red_sparrow, the_darkest_minds]

# creating movies site and opening in a web browser
fresh_tomatoes.open_movies_page(movies)
