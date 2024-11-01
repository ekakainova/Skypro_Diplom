import pytest
import allure
from Pages.Main_Page import MainPage
from Pages.Result_of_Search_Page import ResultOfSearch
from Pages.Series_Page import SeriesPage
from Pages.Filters_Page import FiltersPage
from Pages.Auth_Page import AuthPage


@allure.suite('''UI-тесты на проверку сайта "Кинопоиск"''')
@allure.title('''Переход с главной страницы сайта
              в категорию "Сериалы"''')
@pytest.mark.positive_test
@pytest.mark.ui_positive_test
def test_tv_series_category(driver):

    main_page = MainPage(driver)
    main_page.pop_up_ads()

    main_page.tv_series_category()

    series_page = SeriesPage(driver)
    series_types = series_page.list_of_series_types()

    with allure.step('''Проверить, что на открывшейся странице
                     выбранной категории действительно
                     содержится информация о сериалах'''):
        check_phrase = "Все сериалы онлайн"
        assert check_phrase in series_types, f'''Разделы {series_types} на
        странице "Сериалы" не содержат информации о сериалах'''


@allure.suite('''UI-тесты на проверку сайта "Кинопоиск"''')
@allure.title("Поиск конкретного фильма/сериала")
@pytest.mark.positive_test
@pytest.mark.ui_positive_test
def test_search_movie(driver):

    main_page = MainPage(driver)
    main_page.pop_up_ads()

    search_movie = main_page.box_search("Годзилла")
    main_page.button_search_loupe()

    result_page = ResultOfSearch(driver)
    movies_set = result_page.list_of_movies()

    with allure.step('''Проверить, что название фильма,
                     который мы искали, совпадает с названием фильма,
                     полученного в результате поиска.
                     Либо содержится в его названии'''):
        assert search_movie in movies_set, f'''
        Заданного фильма нет среди результатов поиска: {movies_set}'''


@allure.suite('''UI-тесты на проверку сайта "Кинопоиск"''')
@allure.title("Поиск фильма определённого жанра")
@allure.description("Поиск фильмов с параметром жанра 'комедия'")
@pytest.mark.positive_test
@pytest.mark.ui_positive_test
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

    with allure.step('''Проверить, что результаты поиска
                     действительно являются фильмами
                     с указанным жанром'''):
        assert film_genre in list_of_genres


@allure.suite('''UI-тесты на проверку сайта "Кинопоиск"''')
@allure.title('''Поиск при выборе противоречащих
              друг другу фильтров''')
@pytest.mark.negative_test
@pytest.mark.ui_negative_test
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

    with allure.step('''Проверить, что по запросу ничего не найдено.
                     Система выдает информационное сообщение'''):
        expected_message = "К сожалению, по вашему запросу ничего не найдено"
        assert expected_message in info_message


@allure.suite('''UI-тесты на проверку сайта "Кинопоиск"''')
@allure.title("Проверка входа в личный кабинет с пустым полем пароля")
@pytest.mark.negative_test
@pytest.mark.ui_negative_test
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

    with allure.step('''Проверить, что система выдала
                     предупреждающее сообщение'''):
        expected_message = "Пароль не указан"
        assert hint == expected_message, f"Появляется сообщение {hint}"
