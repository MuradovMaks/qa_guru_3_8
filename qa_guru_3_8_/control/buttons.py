from selene import be, have
from selene.support.shared import browser


def gender_radios(gender):
    browser.element(gender).double_click()


def checkbox(check_box_hobby):
    browser.element(check_box_hobby).click()
