from libs.functions.searching_through_partners_list import *
from libs.helpers.random_staff_generators import *
from pages.add_partner import AddPartner

'''Test adds a new partner and assets if it appears on the all partners list'''


def test_add_partner(browser):
    add_partner_form = AddPartner(browser)
    add_partner_form.add_partner_button.click()
    partner_name = random_word(8)
    add_partner_form.add_name_input.input_text(partner_name)
    add_partner_form.add_email_input.input_text(random_mail(6))
    add_partner_form.short_onboarding_checkbox.click()
    add_partner_form.switch_button.click()
    add_partner_form.add_to_index_button.click()
    all_partners_names = searching_through_partners_list(browser)
    assert partner_name in all_partners_names


