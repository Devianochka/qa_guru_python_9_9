import allure
from selene import browser, be, by
from selene.support.shared.jquery_style import s


def test_decorator():
    allure.dynamic.tag("tage")
    allure.dynamic.label("labelity")
    open_browser()
    search_repository('Devianochka/qa_guru_python_9_9')
    open_repository('Devianochka/qa_guru_python_9_9')
    open_issues_tab()
    should_see_issue_with_name("#1")


@allure.step("Открыть главную страницу")
def open_browser():
    browser.open("https://github.com")


@allure.step("Поиск реппозитория {repo}")
def search_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repo).submit()


@allure.step("Открываем репозиторий {repo}")
def open_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем вкладку Issues")
def open_issues_tab():
    s('#issues-tab').click()


@allure.step("Проверяем наличие Issue с навзанием {name}")
def should_see_issue_with_name(name):
    s(by.partial_text(name)).should(be.visible)
