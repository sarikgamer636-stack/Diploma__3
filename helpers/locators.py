from selenium.webdriver.common.by import By


CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
ORDERS_LIST_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")

MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
INGREDIENT = (By.XPATH, "//a[contains(@href, '/ingredient/')]")
INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num')]")
CONSTRUCTOR_BASKET = (By.XPATH, "//span[contains(text(), 'Перетяните булочку сюда (верх)')]")
ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")

INGRIDIENTS_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
INGRIDIENTS_WINDOW_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
MODAL_OVERLAY = (By.CSS_SELECTOR, "[class*='Modal_modal_overlay']")

ORDERS_LIST = (By.XPATH, "//h1[text()='Лента заказов']")
ALL_TIME_ORDERS_FINISHED = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
TODAY_ORDERS_FINISHED = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
IN_PROGRESS = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul")

NAME_INPUT = (By.XPATH, "(//input[@type='text'])[1]")
EMAIL_INPUT = (By.XPATH, "(//input[@type='text'])[2]")
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
LOGIN_EMAIL_INPUT = (By.XPATH, "(//input[@type='text'])[1]")