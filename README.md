Diploma_3. UI-тесты Stellar Burgers

Автотесты  [Stellar Burgers](https://stellarburgers.education-services.ru/)
на Python + Selenium + Pytest. Браузеры: Chrome и Firefox.

Что проверяется:

- переход по клику на «Конструктор»;
- переход по клику на раздел «Лента заказов»;
- если кликнуть на ингредиент, появится всплывающее окно с деталями;
- всплывающее окно закрывается кликом по крестику;
- при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.
- при создании нового заказа счётчик «Выполнено за всё время» увеличивается;
- при создании нового заказа счётчик «Выполнено за сегодня» увеличивается;
- после оформления заказа его номер появляется в разделе «В работе».

Структура:

- `tests/` — тесты
- `pages/` — Page Object
- `helpers/` — урлы, данные, шаги, локаторы
- `conftest.py` — фикстуры Chrome и Firefox
Пользователь для заказа создаётся через API и удаляется после теста.

Запуск:

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest tests -v --alluredir=allure-results

Отчёты:

allure serve allure-results