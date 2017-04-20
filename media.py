import webbrowser

class Movie():
    """ This class stores movies related inforamtion"""
    #Implement init function
    def __init__(self, movie_title, movie_storyline, poster, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

