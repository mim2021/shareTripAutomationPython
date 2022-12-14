import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HotelBooking:
    def __init__(self, driver):
        self.driver = driver
        self.hotelTab = "//div[@class='tabpanel']//button[text()='Hotel']"
        self.enterCity = "//input[@id='hotelAutocomplete']"
        self.checkInDate = "//input[@id='startDateId']"
        self.checkOutDate = "//input[@id='endDateId']"
        self.guestAndRoomField = "(//div[contains(@class, 'search-group')])[3]"
        self.searchButton = "//body/div[@id='__next']/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/button[1]"

    def click_hotel_tab(self):
        ele1 = self.driver.find_element(By.XPATH, self.hotelTab)
        self.driver.execute_script("arguments[0].click();", ele1)

    def enter_city_input(self, city_name):
        self.driver.find_element(By.XPATH, self.enterCity).click()
        self.driver.find_element(By.XPATH, self.enterCity).send_keys(city_name)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()

    def click_enter_city(self):
        self.driver.find_element(By.XPATH, self.guestAndRoomField).click()

    def search_button(self):
        ele1 = self.driver.find_element(By.XPATH, self.searchButton).click()
        self.driver.execute_script("arguments[0].click();", ele1)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()


























