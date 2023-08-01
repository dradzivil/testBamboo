from selenium.webdriver.common.by import By

class BookPageLocators:
    CREATE_BOOK = (By.CSS_SELECTOR, 'span[style*="color: rgb(250, 250, 250);"]')
    DATE_OF_BOOK = (By.XPATH, '//div[@style="display: flex; gap: 10px;"]/div[1]/input')
    TIME_OF_BOOK = (By.XPATH, '//div[@style="display: flex; gap: 10px;"][1]/div[2]/input')
    DURATION = (By.XPATH, '//div[@style="display: flex; gap: 10px;"][2]/div[2]/input')
    HALL = (By.XPATH, '//div[@style="display: flex; flex-direction: column; gap: 10px;"]/select[@class="selectInput"][1]')
    SCHEME = (By.XPATH, '//div[@style="display: flex; flex-direction: column; gap: 10px;"]/select[@class="selectInput"][2]')
    TABLE = (By.XPATH, '//div[@style="display: flex; flex-direction: column; gap: 10px;"]/select[@class="selectInput"][3]')
    NAME_GUEST = (By.CSS_SELECTOR, 'input[name="Имя гостя"]')
    PHONE = (By.CSS_SELECTOR, 'input[name="Номер телефона"]')
    COMMENTS = (By.CSS_SELECTOR, 'textarea[name="Комментарий"]')
    COUNT_OF_GUESTS = (By.XPATH, '//div[@class="counterInput"]/input')
    BUTTON_SAVE = (By.CSS_SELECTOR, 'div[style="position: absolute; width: 160px; height: 40px; bottom: 20px; right: 20px;"]')