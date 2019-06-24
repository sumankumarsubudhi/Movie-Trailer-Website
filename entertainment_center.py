import fresh_tomatoes
import media


def main():
    """list of my 5 favorite movies"""
    """In the order of movie_name,storyline,poster_image,youtube_tailer_url"""

    deadpool = media.Movie(
        "Deadpool",
        "A fast-talking mercenary subjected to rogue experiment "
        "leaves him with accelerated powers",
        "http://bit.ly/2eorTC7",
        "https://www.youtube.com/watch?v=gtTfd6tISfw")

    avatar = media.Movie(
        "Avatar",
        "A marine on an alien planet.",
        "http://upload.wikimedia.org/wikipedia/id/b/b0/"
        "Avatar-Teaser-Poster.jpg",
        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

    matrix = media.Movie(
        "Matrix",
        "A computer hacker learns from mysterious rebels about the true nature"
        " of his reality and his role in the war against its controllers.",
        "https://www.movieposter.com/posters/archive/main/9/A70-4902",
        "https://www.youtube.com/watch?v=m8e-FF8MsqU")

    contact = media.Movie(
        "Contact",
        "We make contact with aliens",
        "https://upload.wikimedia.org/wikipedia/en/7/75/Contact_ver2.jpg",
        "https://www.youtube.com/watch?v=d9C2cF3KvP8")

    spectre = media.Movie(
        "Spectre",
        "James Bond receives an obscure message he uncovers the conspiracy,",
        "https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg",
        "https://www.youtube.com/watch?v=vBnGxAkdh_k")

    """Storing the list of objects to movies"""
    movies = [deadpool, avatar, matrix, contact, spectre]
    """ opening the trailer webpage in user's web browser"""

    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()
