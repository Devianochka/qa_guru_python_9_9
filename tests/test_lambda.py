import allure
from allure_commons.types import Severity
from selene import browser, be, by
from selene.support.shared.jquery_style import s


@allure.feature("QAGuru")
@allure.description("Homework")
@allure.story("Работаем с allure")
@allure.label("owner", "Devianochka")
@allure.severity(Severity.CRITICAL)
@allure.link("http://github.com", name="github")
def test_lambda_github():
    with allure.step("Открываем страницу Github"):
        browser.open("https://github.com")

    with allure.step("Поиск реппозитория"):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('Devianochka/qa_guru_python_9_9').press_enter()

    with allure.step("Открываем репозиторий"):
        s(by.link_text("Devianochka/qa_guru_python_9_9")).click()

    with allure.step("Открываем вкладку Issues"):
        s('#issues-tab').click()

    with allure.step("Проверяем наличие Issue"):
        s(by.partial_text("#1")).should(be.visible)
