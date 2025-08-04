from selenium.webdriver.common.by import By

class UrbanRoutesLocators:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    search_button = (By.XPATH, "//button[text()='Pedir un taxi']")
    button_comfort = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']/ancestor::div[contains(@class, 'tcard')]")
    button_phone_number = (By.CLASS_NAME, "np-text")
    add_phone_number = (By.NAME, "phone")
    click_btn_siguiente = (By.XPATH, "//button[text()='Siguiente']")
    input_code = (By.ID, "code")
    click_btn_confirmar = (By.XPATH, "//button[text()='Confirmar']")
    metodo_pago = (By.CLASS_NAME, "pp-button")
    agregar_tarjeta = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    input_tarjeta = (By.ID, "number")
    input_codigo = (By.NAME, "code")
    agregar_button = (By.XPATH, "//button[@type='submit' and contains(@class,'button') and normalize-space(text())='Agregar']")
    close_btn = (By.XPATH,
        "//div[contains(@class,'section') and .//div[text()='Método de pago']]//button[contains(@class,'close-button') and contains(@class,'section-close')]")
    comment_input = (By.NAME, "comment")
    manta_panuelos =  (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    ice_cream = (By.XPATH, "//div[contains(@class,'counter-plus')]")
    pedir_taxi_button =     (By.XPATH,
    "//button[.//span[@class='smart-button-main' and normalize-space()='Pedir un taxi']]")
    driver_modal = (By.XPATH, "//div[contains(@class, 'order-header-title') and contains(text(), 'El conductor llegará en')]")