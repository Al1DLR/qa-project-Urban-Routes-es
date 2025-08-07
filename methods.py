from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators import UrbanRoutesLocators


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = UrbanRoutesLocators

    def set_from(self, from_address):
        from_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.from_field)
        )
        from_input.clear()
        from_input.send_keys(from_address)

    def set_to(self, to_address):
        to_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.to_field)
        )
        to_input.clear()
        to_input.send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    def click_pedir_taxi(self):
        self.driver.find_element(*self.locators.search_button).click()

    def click_comfort_button(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.button_comfort)
        )
        btn.click()
        class_attr = btn.get_attribute("class")
        print(f"CLASE DEL BOTÓN: {class_attr}")  # DEBUG opcional
        return "active" in class_attr or "selected" in class_attr

    def click_phone_number_button(self):
        self.driver.find_element(*self.locators.button_phone_number).click()

    def add_phone_number(self, number):
        input_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.add_phone_number)
        )
        input_field.clear()
        input_field.send_keys(number)

    def click_btn_siguiente(self):
        self.driver.find_element(*self.locators.click_btn_siguiente).click()

    def input_code(self, code):
        code_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.input_code)
        )
        code_input.clear()
        code_input.send_keys(code)

    def click_btn_confirmar(self):
        self.driver.find_element(*self.locators.click_btn_confirmar).click()

    def click_metodo_pago(self):
        self.driver.find_element(*self.locators.metodo_pago).click()
    def click_agregar_tarjeta(self):
        self.driver.find_element(*self.locators.agregar_tarjeta).click()

    def input_tarjeta_completa(self, number, cvv):
        card_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.input_tarjeta)
        )
        card_input.clear()
        card_input.send_keys(number,Keys.TAB)

        cvv_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.input_codigo)
        )
        cvv_input.clear()
        cvv_input.send_keys(cvv, Keys.TAB)

    def click_btn_agregar(self):
        self.driver.find_element(*self.locators.agregar_button).click()

    def click_close_btn(self):
        self.driver.find_element(*self.locators.close_btn).click()

    def add_comment(self, message):
        comment_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.comment_input)
        )
        comment_input.send_keys(message)
        return comment_input.get_attribute('value')

    def click_manta_panuelos(self):
        self.driver.find_element(*self.locators.manta_panuelos).click()

    def add_ice_cream(self, quantity=2):
        ice_cream_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.ice_cream)
        )
        for _ in range(quantity):
            ice_cream_btn.click()
        return True

    def click_pedir_taxi_button(self):
        self.driver.find_element(*self.locators.pedir_taxi_button).click()

    def wait_for_driver_modal(self):
        modal = WebDriverWait(self.driver, 35).until(
            EC.visibility_of_element_located(self.locators.driver_modal)
        )
        return modal.is_displayed()