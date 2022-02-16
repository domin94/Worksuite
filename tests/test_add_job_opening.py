from libs.base_page import BasePage
from libs.helpers.random_staff_generators import random_word
from pages.job_opening import JobOpening


def test_add_job_opening(browser):
    browser.get(BasePage.base_URI + "/marketplace/job-openings/list/?archived=false")
    new_job_opening = JobOpening(browser)
    new_job_opening.new_job_opening_button.click()
    job_title = random_word(8)
    new_job_opening.job_title_input.input_text(job_title)
    new_job_opening.create_job_opening_button.click()
    new_job_opening.back_to_jobs_list.click()
    all_jobs = [new_job_opening.jobs_list.text]
    if len(all_jobs) > 0:
        assert job_title in all_jobs
    else:
        assert False

