import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def first_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/…/…/chromedriver.exe')
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element_by_xpath("//*[@id=\"user-name\"]")
    input_password = driver.find_element_by_xpath("//*[@id=\"password\"]")
    login_button = driver.find_element_by_xpath("//*[@id=\"login-button\"]")

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    # Поиск ссылки элемента позиции магазина и клик по ссылке
    item_name = driver.find_element_by_xpath("//*[@id=\"item_5_title_link\"]/div")
    item_name.click()

    # Поиск кнопки добавления товара и клик по этой кнопке
    item_add_button = driver.find_element_by_xpath("//*[@id=\"add-to-cart-sauce-labs-fleece-jacket\"]")
    item_add_button.click()

    # Поиск кнопки коризины и клик по этой кнопке
    shopping_cart = driver.find_element_by_xpath("//*[@id=\"shopping_cart_container\"]/a")
    shopping_cart.click()

    # Еще один поиск ссылки элемента позиции магазина
    item_name = driver.find_element_by_xpath("//*[@id=\"item_5_title_link\"]/div")
    if item_name.text == "Sauce Labs Fleece Jacket":
        print("Товар пристутствует в корзине")
    else:
        print("Товар отсутствует")

    time.sleep(5)


if __name__ == '__main__':
    first_test()