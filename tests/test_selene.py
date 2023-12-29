from selene import browser, be, by
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com")

    s('.header-search-button').click()
    s('#query-builder-test').send_keys('Devianochka/qa_guru_python_9_9').press_enter()

    s(by.link_text("Devianochka/qa_guru_python_9_9")).click()

    s('#issues-tab').click()

    s(by.partial_text("#1")).should(be.visible)
