# Bacon_001_project
# Прогнозирование цен на жилую недвижимость 
## Структура проекта 

Сформулируем наши гипотезы: 
1. Чем больше площадь, тем выше стоимость квартиры.
2. Если в квартире окна выходят во двор, она стоит дороже.
3. Чем больше в квартире жилых комнат, тем больше она ценится.

_Про ML:__ В наших данных есть переменная - цена квартиры, которую мы будем попробовать предсказать. Целевая переменная может принимать любые значения, поэтому мы собираемся делать линейную регрессию.

## Структура репозитария:
1) Парсинг. Папка содержит сам парсер и код с парсингом Авито.
2) data. Папка содержит таблицы со спарсенными данными (final_table) и таблицу соотношения метро c округом и районом (Район).
3) Бекон_Драфт.ipynb. Файл с кодом для промежуточного чекпойнта.
4) Project_final_bacon001.ipynb. Финальный код нашей команды с редакцией таблицы данных, визуализацией, созданием новой переменной (округом), описанием гипотез и их подтверждением/опровержением и использованием машинного обучения.

## Описание спарсенных данных:
1) Тип квартиры: сколько комнат в квартире, является ли она студией и т.д.
2)  м^2
3)  Этаж квартиры.
4)  Сколько этажей в доме.
5)  Адрес.
6)  Станция метро.
7)  Куда выходят окна (во двор, на улицу, на солнечную сторону). Каждой переменной присвоен отдельный столбец в таблице, где 1 указывает на пренадлежность признака квартире, а 0 - на его отсутствие.
8)  Является ли квартира новостройкой. 1 в столбце указывает на пренадлежность признака квартире, а 0 означает, что квартира продается через посредника.
9)  Цена за м^2 квартиры.
10)  Цена квартиры.

Дальнейшее использование этих данных описано в Project_final_bacon001.ipynb.


