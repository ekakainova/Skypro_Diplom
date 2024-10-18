from Pages.Main_Page import MainPage
from Pages.Result_of_Search_Page import ResultOfSearch
from Pages.Series_Page import SeriesPage
from Pages.Filters_Page import FiltersPage
from Pages.Auth_Page import AuthPage

import pytest


# тест на ввод конкретного фильма/сериала
@pytest.mark.positive_test
def test_search_movie(driver):

    main_page = MainPage(driver)
    main_page.pop_up_ads()
    search_movie = main_page.box_search("Годзилла")
    main_page.button_search_loupe()

    result_page = ResultOfSearch(driver)
    movies_set = result_page.list_of_movies()
    print(movies_set)

    assert search_movie in movies_set, f'''
    Заданного фильма нет среди результатов поиска: {movies_set}'''


# тест на выбор категории "Сериалы"
@pytest.mark.positive_test
def test_tv_series_category(driver):

    main_page = MainPage(driver)
    main_page.pop_up_ads()
    main_page.tv_series_category()

    series_page = SeriesPage(driver)
    series_types = series_page.list_of_series_types()

    check_phrase = "Все сериалы онлайн"

    assert check_phrase in series_types, f'''Разделы {series_types} на
    странице "Сериалы" не содержат информации о сериалах'''


# выбор определенного жанра в фильтрах
@pytest.mark.positive_test
def test_genre_filter(driver):

    main_page = MainPage(driver)
    main_page.pop_up_ads()
    main_page.button_of_filters()

    filter_page = FiltersPage(driver)
    film_genre = filter_page.list_of_genres("комедия")
    filter_page.what_looking_for("фильм")
    filter_page.button_search_one()

    result_page = ResultOfSearch(driver)
    list_of_genres = result_page.list_of_genres_movies()

    assert film_genre in list_of_genres


# вход с пустым полем пароля
@pytest.mark.negative_test
def test_empty_password_field(driver):

    main_page = MainPage(driver)
    main_page.pop_up_ads()
    main_page.button_login()

    auth_page = AuthPage(driver)
    auth_page.login_field("so4nayavishenka@yandex.ru")
    auth_page.button_sign_in_one()
    auth_page.button_password()
    auth_page.password_field("")
    hint = auth_page.button_sign_in_two()

    expected_message = "Пароль не указан"

    assert hint == expected_message, f"Появляется сообщение {hint}"


# тест на выбор противоречащих фильтров
@pytest.mark.negative_test
def test_conflicting_filters(driver):

    main_page = MainPage(driver)
    main_page.pop_up_ads()
    main_page.button_of_filters()

    filter_page = FiltersPage(driver)
    filter_page.MPAA_system("PG-13")
    filter_page.list_of_genres("для взрослых")
    filter_page.button_search_one()

    result_page = ResultOfSearch(driver)
    info_message = result_page.list_of_movies()

    expected_message = "К сожалению, по вашему запросу ничего не найдено"

    assert expected_message in info_message
