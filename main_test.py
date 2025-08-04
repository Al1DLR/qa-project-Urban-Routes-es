import json
import time
import data as data
from methods import UrbanRoutesPage
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options


def retrieve_phone_code(driver) -> str:
    code = None
    for _ in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if code:
            return code
    raise Exception("No se encontró el código de confirmación del teléfono.")


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        options = Options()
        # Configura los logs de rendimiento (performance logs)
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()


    def test_full_taxi_order(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)

        # Configurar ruta
        page.set_route(data.address_from, data.address_to)
        assert page.get_from() == data.address_from
        assert page.get_to() == data.address_to

        # Pedir un taxi
        page.click_pedir_taxi()

        # Seleccionar tarifa Comfort
        page.click_comfort_button()

        # Número de teléfono y confirmación
        page.click_phone_number_button()
        page.add_phone_number(data.phone_number)
        page.click_btn_siguiente()

        code = retrieve_phone_code(self.driver)
        page.input_code(code)
        page.click_btn_confirmar()

        # Método de pago y tarjeta
        page.click_metodo_pago()
        page.click_agregar_tarjeta()
        page.input_tarjeta_completa(*data.card_number)

        #click en el boton de agregar
        page.click_btn_agregar()

        #cerrar ventana agregar pago
        page.click_close_btn()


        # Mensaje para el conductor
        page.add_comment(data.message_for_driver)

        # Pedir manta y pañuelos
        page.click_manta_panuelos()

        # Pedir 2 helados
        page.add_ice_cream(2)

        # Confirmar pedido
        page.pedir_taxi_button()

        # Esperar modal con info del conductor
        page.wait_for_driver_modal()
        assert self.driver.find_element(*page.locators.driver_modal).is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()