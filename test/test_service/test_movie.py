import pytest
from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_all(self):
        movie = self.movie_service.get_all()
        assert movie is not None
        assert len(movie) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
        assert movie.title == "one + one"
        assert movie.genre_id is not None
        assert movie.year is not None
        assert movie.director_id is not None
        assert movie.trailer is not None
        assert movie.rating is not None

    def test_create(self):
        movie_d = {
            "title": "Movie 4",
            "description": "Description 4",
            "trailer": "link 4",
            "year": 2020,
            "rating": 5.0,
            "genre_id": 4,
            "director_id": 4,
        }

        genre = self.movie_service.create(movie_d)
        assert genre.id is not None

    def test_update(self):
        movie_d = {
            "id": 1,
            "title": "Movie 4",
            "description": "Description 4",
            "trailer": "link 4",
            "year": 2020,
            "rating": 5.0,
            "genre_id": 4,
            "director_id": 4,
        }
        assert self.movie_service.update(movie_d)

    def test_delete(self):
        assert self.movie_service.delete(1) is None
