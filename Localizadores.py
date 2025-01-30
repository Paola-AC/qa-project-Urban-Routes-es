import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import Codigo_phone
from selenium.webdriver.support import expected_conditions as EC


# Escribir los Localizadores

class UrbanRoutesPage_locators:

# Espera cargue pagina principal
    home_page = (By.ID, "root")

# Configurar la direccion
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

# Click en el boton "Pedir un taxi"
    order_taxi_btn = (By.CSS_SELECTOR, ".button.round")

# Esperar hasta que aparezca el tablero con las opciones de tarifa
    board_rate_options =(By.CLASS_NAME, "tariff-cards")

# Seleccionar tarifa "Comfort"
    Comfort_rate = (By.XPATH, "//div[@class='tcard-title'][text()='Comfort']")

# Agregar Numero de Telefono
    phone_number_btn = (By. CSS_SELECTOR, ".np-text")
    add_phone_number = (By. ID, 'phone')
    next_phone_number_btn = (By.XPATH, "//*[@class='button full'][text( )= 'Siguiente']")

# Ingresar el Codigo del SMS y Confirmar
    enter_phone_code = (By.ID, 'code')
    confirm_phone_code_btn = (By.XPATH, "//*[@class='button full'][text( )= 'Confirmar']")


# Ingresar Metodo de Pago - Tarjeta
    paymenth_method_btn = (By.CSS_SELECTOR, ".pp-text")
    Add_card_details = (By.XPATH, "//*[@class='pp-title'][text( )= 'Agregar tarjeta']")
    card_Number_input = (By.ID, 'number')
    Add_card_details_code = (By.CLASS_NAME, 'card-code-input')
    card_code_input = (By.XPATH, "//*[@class='card-input'][@ID='code']")
    Add_card = (By.XPATH, "//*[@class='button full'][text( )= 'Agregar']")
# Tan pronto se da "Agregar" se cierra la ventana "Agregar Tarjeta"
# Ahora, se tiene que cerrar la ventana "Metodo de pago"
    Close_payment_method = (By. XPATH, "//div[@class='section active']//div[@class='head' and text()='Método de pago']//ancestor::div[@class='section active']//button[@class='close-button section-close']")

# Escribir mensaje al conducto
    select_message_for_driver = (By.CSS_SELECTOR, "label[for='comment']")
    write_message_for_driver = (By.XPATH, "//*[@class='input'][@ID='comment']")

# Requisitos del pedido
# 1. Pedir una manta y panuelos
    request_manta_panuelos = (By.XPATH, "//div[text()='Manta y pañuelos']//following-sibling::div//span[@class='slider round']")
# 2. Pedir 2 Helados (si el contador ya tiene algun numero esto puede cambiar)
    request_ice_cream = (By.XPATH, "//div[text()='Helado']//following-sibling::div//div[@class='counter-plus']")

# Reservar un taxi
    book_taxi = (By.CLASS_NAME, "smart-button-wrapper")

# Esperar hasta que aparezca el modal de conductor asignado
    wait_select_driver = (By.CSS_SELECTOR, ".order-header-content")








