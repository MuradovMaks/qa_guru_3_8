from selene import be, have
from selene.support.shared import browser
from qa_guru_3_8_.control.datepickers import datepickers_value
from qa_guru_3_8_.control.buttons import gender_radios, checkbox
from qa_guru_3_8_.control.dropdown import subjects, dropdowns_home


def open_website(website):
    browser.open(website)


def submit(submit):
    browser.element(submit).submit()


def data_for_submit(option, values):
    browser.element(option).should(be.blank).type(values)


def datepicker_alert():
    datepickers_value()


def buttons():
    gender_radios()
    checkbox()


def dropdowns():
    subjects()
    dropdowns_home()


def research_text_from_modal(option, values):
    browser.element(option).should(have.text(values))
