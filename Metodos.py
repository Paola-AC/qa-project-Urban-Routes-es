import data
from data import card_number, card_code
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Localizadores import UrbanRoutesPage_locators
import time
from Codigo_phone import retrieve_phone_code
from selenium.webdriver.support import expected_conditions as EC




# Escribir los Metodos
class UrbanRoutesPage_Methods:

    def __init__(self, driver):
        self.driver = driver
        self.localizadores = UrbanRoutesPage_locators()

# Cargue de pagina
    def wait_for_load_home_page(self,):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(self.localizadores.home_page))

# Configurar la direccion
    def set_from(self,):
        self.driver.find_element(*self.localizadores.from_field).send_keys(data.address_from)

    def set_to(self,):
        self.driver.find_element(*self.localizadores.to_field).send_keys(data.address_to)

    def get_from(self):
        return self.driver.find_element(*self.localizadores.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.localizadores.to_field).get_property('value')

# Click en el boton "Pedir un taxi"
    def click_order_taxi_btn(self):
        self.driver.find_element(*self.localizadores.order_taxi_btn).click()

# Esperar hasta que aparezca el tablero con las opciones de tarifa
    def wait_board_rate_options(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.localizadores.board_rate_options))

# Seleccionar tarifa "Comfort"
    def click_comfort_rate_btn(self):
        self.driver.find_element(*self.localizadores.Comfort_rate).click()

# Campo - Numero de Telefono
# Seleccionar campo Numero de Telefono
    def click_phone_number_btn(self):
        self.driver.find_element(*self.localizadores.phone_number_btn).click()

# Rellenar campo con el numero de telefono
    def set_phone_field(self):
        self.driver.find_element(*self.localizadores.add_phone_number).send_keys(data.phone_number)
        time.sleep(3)

# Dar click en Boton siguiente y solicitar el codigo de confirmacion
    def click_next_phone_number_btn(self):
        self.driver.find_element(*self.localizadores.next_phone_number_btn).click()

# Rellenar el Codigo SMS y Confirmar
    # Esperar hasta que el campo de código de confirmación sea visible
    def wait_confirmation_modal(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.localizadores.enter_phone_code))

    # Ingresar el código de confirmación en el campo
    def wait_confirmation_code_input(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.localizadores.enter_phone_code))

    def enter_code_input(self,code):
        self.driver.find_element(*self.localizadores.enter_phone_code).send_keys(code)

    def click_confirm_phone_code_btn(self):
        self.driver.find_element(*self.localizadores.confirm_phone_code_btn).click()


# Ingresar Metodo de Pago - Tarjeta de Credito
    def click_paymenth_method_btn(self):
        self.driver.find_element(*self.localizadores.paymenth_method_btn).click()
        time.sleep(3)

# En la nueva ventana, click en el boton agregar tarjeta
    def click_Add_card_details(self):
        self.driver.find_element(*self.localizadores.Add_card_details).click()

# En la siguiente ventana, rellenar los campos "Numero de Tarjeta" y "Codigo" y desbloquea la pantalla
    def set_card_Number_input(self,prueba_card_number):
        self.driver.find_element(*self.localizadores.card_Number_input).send_keys(prueba_card_number+Keys.TAB)

    def click_Add_card_details_code(self):
        self.driver.find_element(*self.localizadores.Add_card_details_code).click()

    def set_card_code_input(self,prueba_card_code):
        self.driver.find_element(*self.localizadores.card_code_input).send_keys(prueba_card_code)

# Dar click en el bonton "Agregar"
    def click_Add_card(self):
        self.driver.find_element(*self.localizadores.Add_card).click()

# Cerrar la ventana "Metodo de pago"
    def click_close_payment_method(self):
        self.driver.find_element(*self.localizadores.Close_payment_method).click()

# Rellenar mensaje para el conductor
    def click_select_message_for_driver(self):
        self.driver.find_element(*self.localizadores.select_message_for_driver).click()

    def set_write_message_for_driver(self):
        self.driver.find_element(*self.localizadores.write_message_for_driver).send_keys(data.message_for_driver)

# Requisitos adicionales al pedido
# 1. Solicitar manta y panuelos
    def click_request_manta_panuelos(self):
        self.driver.find_element(*self.localizadores.request_manta_panuelos).click()

# 2. Pedir 2 Helados, dar dos veces click en el bonton "+"
    def click_request_ice_cream(self):
        self.driver.find_element(*self.localizadores.request_ice_cream).click()

# Reservar un taxi
    def click_book_taxi(self):
        self.driver.find_element(*self.localizadores.book_taxi).click()

# Esperar hasta que aparezca el modal de conductor asignado
    def wait_select_driver_modal(self):
        WebDriverWait(self.driver, 35).until(EC.visibility_of_element_located(self.localizadores.wait_select_driver))
