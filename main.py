import data
from data import card_number, card_code
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Metodos import UrbanRoutesPage_Methods
import time
from Codigo_phone import retrieve_phone_code



# Escribir las pruebas
class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        # Inicializar el WebDriver con las opciones
        cls.driver = webdriver.Chrome(options=options)

        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage_Methods(cls.driver)
        time.sleep(7)


# Prueba_1 para configurar la direccion y dar click en boton "Pedir un Taxi"
    def test_set_route(self):
        self.routes_page.set_from()
        self.routes_page.set_to()
        time.sleep(3)
        self.routes_page.click_order_taxi_btn()
        self.routes_page.wait_board_rate_options()


# assert self.routes_page.set_from() == data.address_from
# assert self.routes_page.set_to() == data.address_to

# Prueba_2 Elegir la tarifa "Comfort"
    def test_select_rate(self):
        self.routes_page.click_comfort_rate_btn()


# Prueba_3 Rellenar el campo "Numero de telefono"
    def test_fill_phone_number(self):
        # Hacer clic en el botón para ingresar el teléfono
        self.routes_page.click_phone_number_btn()
        self.routes_page.set_phone_field()
        self.routes_page.click_next_phone_number_btn()

        # Esperar hasta que el campo de código de confirmación sea visible
        self.routes_page.wait_confirmation_modal()

        # Obtener el código de confirmacion
        self.codigo_phone = retrieve_phone_code(self.driver)

       # Ingresar el código de confirmación en el campo
        self.routes_page.enter_code_input(self.codigo_phone)

        # Hacer clic en el botón de confirmación del código
        self.routes_page.click_confirm_phone_code_btn()

    def test_fill_paymenth_method(self):
        self.routes_page.click_paymenth_method_btn()
        self.routes_page.click_Add_card_details()
        self.routes_page.set_card_Number_input(data.card_number)
        time.sleep(2)
        self.routes_page.click_Add_card_details_code()
        self.routes_page.set_card_code_input(data.card_code+Keys.TAB)
        self.routes_page.click_Add_card()
        self.routes_page.click_close_payment_method()
        time.sleep(5)

    def test_fill_message_for_driver(self):
        self.routes_page.click_select_message_for_driver()
        self.routes_page.set_write_message_for_driver()
        time.sleep(3)

    def test_order_blanket_and_tissues(self):
        self.routes_page.click_request_manta_panuelos()
        time.sleep(3)

    def test_order_dos_ice_cream(self):
        self.routes_page.click_request_ice_cream()
        self.routes_page.click_request_ice_cream()
        time.sleep(2)

    def test_fill_order_a_taxi(self):
        self.routes_page.click_book_taxi()
        self.routes_page.wait_select_driver_modal()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
