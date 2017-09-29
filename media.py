import webbrowser
# This is a class named movies
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
    	"""
    	This is a function which contains all the details of the movie where=>
    	self: This points to a particluar movie.
    	movie_title:It represents the movie title.
    	movie_story_line: It represents the movie story line.
    	poster_image: It represents the poster image.
    	trailer_youtube: It represents the youtube trailer of that particluar movie.
    	Output=>
    	It returns the movie title, movie storyline, poster image and the youtube trailer of the selected movie.
 		"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def open_trailer(self):
    	"""
    	This function is used to display the trailer of the movie.
    	Output: It opens the youtube trailer of the particluar selected movie.
    	"""
    	webbrowser.open(self.trailer_youtube_url)
