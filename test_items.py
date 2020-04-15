import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_cart_button_exists(browser):
    browser.get(link)
    time.sleep(30)
    cart_button_name = browser.find_element_by_css_selector(".btn-add-to-basket").get_attribute("value")
    print(f'\n Cart button name is: {cart_button_name}')  # use -s parameter when execute the test
    assert cart_button_name == "Añadir al carrito", "Not Spanish localization"


