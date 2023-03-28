from selene import be, have
from selene.support.shared import browser
import os
from qa_guru_3_8_.usual_steps import practice_form_modules
from qa_guru_3_8_.control import jpegs


def test_practice_form_pg(open_browser):
    practice_form_modules.open_website('https://demoqa.com/automation-practice-form')
    practice_form_modules.data_for_submit('#firstName', 'Max')
    practice_form_modules.data_for_submit('[id=lastName]', 'Muradov')
    practice_form_modules.data_for_submit('[id=userEmail]', 'koreantech620@mail.ru')
    practice_form_modules.data_for_submit('[id=userNumber]', '0790345439')
    practice_form_modules.datepickers_value('#dateOfBirthInput')
    practice_form_modules.datepickers_value('[class ="react-datepicker__month-select"] >[value="3"]')
    practice_form_modules.datepickers_value('[class="react-datepicker__year-select"] >[value="2000"]')
    practice_form_modules.datepickers_value('[class="react-datepicker__day react-datepicker__day--024"]')
    practice_form_modules.gender_radios(gender='[id=gender-radio-1]')
    practice_form_modules.checkbox(check_box_hobby='[for="hobbies-checkbox-1"]')
    practice_form_modules.data_for_submit('[id="currentAddress"]', 'Greenwich Time')
    practice_form_modules.subjects('[id="subjectsInput"]', 'Hindi')
    practice_form_modules.dropdowns_home('[id="react-select-3-input"]', 'NCR')
    practice_form_modules.dropdowns_home('[id="react-select-4-input"]', 'Noida')
    jpegs.icon('#uploadPicture', 'jpegi/1614256626_python_logo.jpg')
    practice_form_modules.submit("[id = submit]")
    practice_form_modules.research_text_from_modal(
        '[class="table table-dark table-striped table-bordered table-hover"]',
        "Max Muradov" and
        "koreantech620@mail.ru" and
        "Male" and
        "0790345439" and
        "24 April,2000" and
        "Hindi" and
        "Sports" and
        "1614256626_python_logo.jpg" and
        "Grrenwich Time" and
        "NCR Noida"
    )
HELLO WORLD