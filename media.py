import webbrowser


class Movie():
    """
    'self' keyword we can access the attributes and
    methods of the class in python for __init__
    Arguments:
    parameter 1: address the movie_title
    parameter 2: pops up the storyline with respective movie
    parameter 3: shows poster of the movie
    parameter 4: URL for trailer of the movie
    """
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        # movie name
        self.title = movie_title
        # movie storyline
        self.storyline = movie_storyline
        # movie poster image url to access
        self.poster_image_url = poster_image
        # movie trailer url to access
        self.trailer_youtube_url = trailer_youtube
        # self - access the python classes

    def show_trailer(self):
        """self - refers to a variable field within the class
        this function show_trailer(self) shows up trailer
        self is used as a strong convention"""
        webbrowser.open(self.trailer_youtube_url)
