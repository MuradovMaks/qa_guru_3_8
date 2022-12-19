from selene.support.shared import browser
import os


def icon(selector_icon, file):
    browser.element(selector_icon).set_value(
        os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, file))
