from selene.support.shared import browser


def datepickers_value(selctor_datepicker):
    browser.element(selctor_datepicker).click()
