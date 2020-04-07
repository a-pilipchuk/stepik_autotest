import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    #берём текст, найденный в теге с id input_value:
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element_by_css_selector("#answer")
    input_answer.send_keys(y)
    chckbx = browser.find_element_by_css_selector("#robotCheckbox")
    chckbx.click()
    rdbttn = browser.find_element_by_css_selector("#robotsRule")
    rdbttn.click()
    submit_bttn = browser.find_element_by_css_selector(".btn-default")
    submit_bttn.click()

finally:
    time.sleep(5)
    browser.quit()
