import pytest
import allure


@allure.suite('''API-тесты на проверку сайта "Кинопоиск"''')
@allure.title("Поиск фильма по названию на кириллице")
@pytest.mark.positive_test
@pytest.mark.api_positive_test
def test_cyrillic_movie_search(api):

    movie_name = 'Годзилла'
    search_info = api.search_movie(movie_name)

    with allure.step('''Получить название первого
                     фильма в списке результа поиска'''):
        result = search_info['docs'][0]['name']

    with allure.step('''Проверить, что название фильма,
                     который мы искали, совпадает с названием фильма,
                     полученного в результате поиска.
                     Либо содержится в его названии'''):
        assert movie_name in result


@allure.suite('''API-тесты на проверку сайта "Кинопоиск"''')
@allure.title("Поиск фильма по id")
@pytest.mark.positive_test
@pytest.mark.api_positive_test
def test_search_movie_by_id(api):

    movie_name = 'Годзилла'
    search_info = api.search_movie(movie_name)

    with allure.step("Получить id найденного фильма"):
        movie_id = search_info['docs'][0]['id']

    movie_info = api.search_by_id(movie_id)

    with allure.step("Получить название найденного по id фильма"):
        result = movie_info['name']

    with allure.step('''Проверить, что название фильма,
                     который мы искали в шаге 1, совпадает с названием фильма,
                     полученного в результате поиска по id'''):
        assert movie_name in result


@allure.suite('''API-тесты на проверку сайта "Кинопоиск"''')
@allure.title("Поиск фильмов определенного жанра")
@allure.description("Поиск фильмов с параметром жанра 'комедия'")
@pytest.mark.positive_test
@pytest.mark.api_positive_test
def test_search_comedies(api):

    movie_type = 'movie'
    movie_genre = 'комедия'
    search_info = api.search_with_filters(movie_type, movie_genre)

    needed_genre = api.get_needed_movie_genres(movie_type, movie_genre)

    with allure.step('''Проверить, что результаты поиска
                     действительно являются фильмами
                     с заданным типом и указанным жанром'''):
        assert movie_type == search_info['docs'][0]['type']
        assert movie_genre == needed_genre


@allure.suite('''API-тесты на проверку сайта "Кинопоиск"''')
@allure.title("Поиск при вводе в поисковую строку только пробелов")
@allure.description('''Ожидаемо падающий тест,
                    так как тело ответа возвращает не пустой список,
                    а список различных фильмов/сериалов''')
@pytest.mark.xfail
@pytest.mark.negative_test
@pytest.mark.api_negative_test
def test_movie_search_with_whitespaces(api):

    movie_name = '      '
    search_info = api.search_movie(movie_name)

    with allure.step("Получить значение длины списка вернувшегося результата"):
        expected_response_body = 0
        actual_response_body = len(search_info['docs'])

    with allure.step('''Проверить, что ожидаемая длина
                     списка равна фактической'''):
        assert expected_response_body == actual_response_body


@allure.suite('''API-тесты на проверку сайта "Кинопоиск"''')
@allure.title('''Поиск при выборе противоречащих
              друг другу фильтров''')
@pytest.mark.negative_test
@pytest.mark.api_negative_test
def test_search_with_wrong_filters(api):

    movie_type = 'movie'
    movie_genre = 'для взрослых'
    movie_rating = 'pg13'
    search_info = api.search_with_filters(
        movie_type, movie_genre, movie_rating)

    with allure.step("Получить значение длины списка вернувшегося результата"):
        expected_response_body = 0
        actual_response_body = len(search_info['docs'])

    with allure.step('''Проверить, что ожидаемая длина
                     списка равна фактической'''):
        assert expected_response_body == actual_response_body
