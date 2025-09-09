# locators/important_questions_locators.py
from selenium.webdriver.common.by import By

class ImportantQuestionsLocators:
    important_quastions_text = (By.XPATH, ".//div[@class='Home_SubHeader__zwi_E']")

    question_price_scooter = (By.ID, 'accordion__heading-0')
    question_price_scooter_text = (By.ID, 'accordion__panel-0')

    question_time_scooter = (By.ID, 'accordion__heading-1')
    question_time_scooter_text = (By.ID, 'accordion__panel-1')

    question_multiple_scooter = (By.ID, 'accordion__heading-2')
    question_multiple_scooter_text = (By.ID, 'accordion__panel-2')

    question_order_scooter_today = (By.ID, 'accordion__heading-3')
    question_order_scooter_today_text = (By.ID, 'accordion__panel-3')

    question_extend_scooter = (By.ID, 'accordion__heading-4')
    question_extend_scooter_text = (By.ID, 'accordion__panel-4')

    question_charge_scooter = (By.ID, 'accordion__heading-5')
    question_charge_scooter_text = (By.ID, 'accordion__panel-5')

    question_cancel_order = (By.ID, 'accordion__heading-6')
    question_cancel_order_text = (By.ID, 'accordion__panel-6')

    question_mkad_scooter = (By.ID, 'accordion__heading-7')
    question_mkad_scooter_text = (By.ID, 'accordion__panel-7')
