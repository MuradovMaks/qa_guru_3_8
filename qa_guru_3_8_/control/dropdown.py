from selene import be, have
from selene.support.shared import browser


def subjects(language, type_lang):
    browser.element(language).type(type_lang).press_enter()


def dropdowns_home(option, value):
    browser.element(option).type(value).press_enter()
    browser.element(option).type(value).press_enter()
