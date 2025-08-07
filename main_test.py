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
    drive = None

    @classmethod
    def setup_class(cls):
        options = Options()
        # Configura los logs de rendimiento (performance logs)
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()
        cls.driver.get(data.urban_routes_url)
        cls.page = UrbanRoutesPage(cls.driver)


    def test_input_address(self):

        # Configurar ruta
        self.page.set_route(data.address_from, data.address_to)
        assert self.page.get_from() == data.address_from
        assert self.page.get_to() == data.address_to

        # Pedir un taxi
    def test_pedir_taxi_y_tarifa(self):
        self.page.click_pedir_taxi()
        is_selected =self.page.click_comfort_button()
        assert is_selected, "No se seleccionó la tarifa Comfort"
        # Número de teléfono y confirmación
    def test_add_phone_number(self):
        self.page.click_phone_number_button()
        self.page.add_phone_number(data.phone_number)
        self.page.click_btn_siguiente()
        code = retrieve_phone_code(self.driver)
        self.page.input_code(code)
        self.page.click_btn_confirmar()
        assert not self.driver.find_element(*self.page.locators.input_code).is_displayed()
        # Método de pago y tarjeta
    def test_metodo_de_pago(self):
        self.page.click_metodo_pago()
        self.page.click_agregar_tarjeta()
        self.page.input_tarjeta_completa(data.card_number["number"], data.card_number["cvv"])
        #clic en el boton de agregar
        self.page.click_btn_agregar()

        #cerrar ventana agregar pago
        self.page.click_close_btn()


        # Mensaje para el conductor
    def test_mensaje_conductor(self):
        message_sent = self.page.add_comment(data.message_for_driver)
        assert message_sent == data.message_for_driver
        # Pedir manta y pañuelos
    def test_pedir_manta_panuelo(self):
        self.page.click_manta_panuelos()
        assert True
    def test_pedir_helado(self):
        self.page.add_ice_cream(2)
        assert self.page.add_ice_cream(quantity=2)

        # Confirmar pedido
    def test_confirmar_pedido(self):
        self.page.click_pedir_taxi_button()


        # Esperar modal con info del conductor
    def test_modal_conductor(self):
        is_displayed = self.page.wait_for_driver_modal()
        assert is_displayed,"No se mostró el modal del conductor"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()