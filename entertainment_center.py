import media
import fresh_tomatoes

pursuit_of_happyness = media.Movie("Pursuit of happyness","Life is a struggle for single father Chris Gardner (Will Smith). Evicted from their apartment, he and his young son (Jaden Christopher Syre Smith) find themselves alone with no place to go. Even though Chris eventually lands a job as an intern at a prestigious brokerage firm, the position pays no money. The pair must live in shelters and endure many hardships, but Chris refuses to give in to despair as he struggles to create a better life for himself and his son.","http://www.impawards.com/2006/posters/pursuit_of_happyness.jpg","https://www.youtube.com/watch?v=SIZKoak6gp8")

forrest_gump = media.Movie("Forrest Gump","Slow-witted Forrest Gump (Tom Hanks) has never thought of himself as disadvantaged, and thanks to his supportive mother (Sally Field), he leads anything but a restricted life. Whether dominating on the gridiron as a college football star, fighting in Vietnam or captaining a shrimp boat, Forrest inspires people with his childlike optimism. But one person Forrest cares about most may be the most difficult to save -- his childhood love, the sweet but troubled Jenny (Robin Wright).","https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UY268_CR10,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=EtYNngO7eq4")

hachi = media.Movie("Hachi","A Dog's tale","http://www.sonypictures.com/movies/hachiadogstale/assets/images/onesheet.jpg","https://www.youtube.com/watch?v=JImj5lV7al4")

panda = media.Movie("Kung fu Panda","Po the panda (Jack Black) works in his family's noodle shop and dreams of becoming a kung-fu master. His dream becomes a reality when, unexpectedly, he must fulfill an ancient prophecy and study the skills with his idols, the Furious Five. Po needs all the wisdom, strength and ability he can muster to protect his people from an evil snow leopard","https://resizing.flixster.com/nA0UOjQRyo3nZmtiMD1b5rQGe6g=/206x305/v1.bTsxMTE3Nzg0MztqOzE3MzY0OzEyMDA7ODAwOzEyMDA","https://www.youtube.com/watch?v=tuOA5WZVQRQ")

walter_mitty = media.Movie("The secret life of Walter Mitty","Walter Mitty (Ben Stiller), an employee at Life magazine, spends day after monotonous day developing photos for the publication. To escape the tedium, Walter inhabits a world of exciting daydreams in which he is the undeniable hero. Walter fancies a fellow employee named Cheryl (Kristen Wiig) and would love to date her, but he feels unworthy. However, he gets a chance to have a real adventure when Life's new owners send him on a mission to obtain the perfect photo for the final print issue.","https://resizing.flixster.com/FEIILRoZa_GsQOIW_Z9Gwyh1whQ=/206x305/v1.bTsxMTE3NzM1NDtqOzE3MzY0OzEyMDA7ODAwOzEyMDA","https://www.youtube.com/watch?v=5I6T_WztBXg")

hunger_games = media.Movie("Hunger Games","In what was once North America, the Capitol of Panem maintains its hold on its 12 districts by forcing them each to select a boy and a girl, called Tributes, to compete in a nationally televised event called the Hunger Games. Every citizen must watch as the youths fight to the death until only one remains. District 12 Tribute Katniss Everdeen (Jennifer Lawrence) has little to rely on, other than her hunting skills and sharp instincts, in an arena where she must weigh survival against love.","https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=FovFG3N_RSU")

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)

movies = [pursuit_of_happyness,forrest_gump,hachi,panda,walter_mitty,hunger_games]
fresh_tomatoes.open_movies_page(movies)
