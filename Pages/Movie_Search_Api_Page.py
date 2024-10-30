import requests
import allure


class Movie_Search:

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    @allure.step("api. Найти все фильмы по названию: {movie_name}")
    def search_movie(self, movie_name, page=1, limit=10):
        my_params = {
            'page': page,
            'limit': limit,
            'query': movie_name
        }

        my_headers = {
            'accept': 'application/json'
        }
        my_headers['X-API-KEY'] = self.api_key

        resp = requests.get(
            self.url + '/movie/search', params=my_params, headers=my_headers)
        return resp.json()

    @allure.step("api. Поиск фильма по id = {movie_id}")
    def search_by_id(self, movie_id):
        my_headers = {
            'accept': 'application/json'
        }
        my_headers['X-API-KEY'] = self.api_key

        resp = requests.get(
            self.url + '/movie/' + str(movie_id), headers=my_headers)
        return resp.json()

    @allure.step('''api. Поиск фильма с приминением
                 следующих фильтров: тип фильма - {type},
                 жанр фильма - {genre}, рейтинг MPAA - {ratingMPAA}''')
    def search_with_filters(
            self, type, genre, ratingMPAA='', page=1, limit=10):
        my_params = {
            'page': page,
            'limit': limit,
            'type': type,
            'genres.name': genre,
            'ratingMpaa': ratingMPAA
        }

        my_headers = {
            'accept': 'application/json'
        }
        my_headers['X-API-KEY'] = self.api_key

        resp = requests.get(
            self.url + '/movie', params=my_params, headers=my_headers)
        return resp.json()

    @allure.step('''api. Найти в описаниях фильмов,
                 полученных в результате поиска,
                 определенный жанр - {need_genre}''')
    def get_needed_movie_genres(self, type, need_genre):
        search_info = self.search_with_filters(type, need_genre)
        list_of_genres = search_info['docs'][0]['genres']
        count_elements = len(list_of_genres)

        for element in range(count_elements):
            value = list_of_genres[int(element)]['name']
            if value == need_genre:
                return value
            else:
                pass
