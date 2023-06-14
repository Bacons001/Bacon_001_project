# Bacon_001_project
# Прогнозирование цен на жилую недвижимость 

## Структура репозитария:
1) Парсинг. Папка содержит сам парсер и код с парсингом Авито.
2) data. Папка содержит таблицы со спарсенными данными (final_table) и таблицу соотношения метро c округом и районом (Район).
3) Бекон_Драфт.ipynb. Файл с кодом для промежуточного чекпойнта.
4) Project_final_bacon001.ipynb. Финальный код нашей команды с редакцией таблицы данных, визуализацией, созданием новой переменной (округом, типом этажа квартиры), описанием гипотез и их подтверждением/опровержением и использованием машинного обучения для подтверждения наших выводов.

## Описание спарсенных данных (или содержание final_table):
Мы брали объявления, представленные на сайте Avito, о продаже квартир Москвы.  

Из этих объявления мы выбрали признаки, которые, по нашему мнению, могли повлиять на итоговую цену квартиры, а также саму цену квартиры, как целевую переменную:
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

## Структура проекта 
Мы обработали спарсенные данные, добавили новую переменную (округ, тип этажа квартиры) и сделали визуализацию представленных данных. 

На основе полученных графиков и коррелиционной таблицы наша команда сформулировала следующие гипотезы: 
1. Чем больше площадь, тем выше стоимость квартиры.
2. Если в квартире окна выходят во двор, она стоит дороже.
3. Чем больше в квартире жилых комнат, тем больше она ценится.
4. Квартиры на первом этаже дешевле, чем квартиры на последнем этаже

Для анализа этих гипотез мы использовали t-тест Стьюдента и коэффициент корреляции Пирсона и считали p-value (брали уровень значимости 0.05). Все наши гипотезы подтвердились.

## Про ML 
Для предсказания цены квартиры мы использовали линейную регрессию, kNN и случайный лес. Эффективность полученных моделей мы проверяли с помощью  среднеквадратической ошибки, средней абсолютной ошибки и коэффициента детерминации.


