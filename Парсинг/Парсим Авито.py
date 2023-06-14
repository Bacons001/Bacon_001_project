from bs4 import BeautifulSoup  
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()

# Настраиваем параметры драйвера, чтобы Авито нас не ловил
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
import pandas as pd

driver = webdriver.Chrome(options=options)

# Создаем списки под все переменные
# Количество страниц для каждой категории рассчитывалась пропорционально общему количеству страниц всех категорий 
# (Т.е. количество квартир с окнами на сол. сторону + новостройка относятся к кол-ву квартир с окнами на солн. сторону + от посредника как 3:6)

prices_per_m_f= []
prices_per_flat_f = []
flat_f = []
m_2_f = []
floor_f = []
floors_f = []
adresses_f = []
stations_f = []
vo_dvor = []
na_ul = []
na_soln = []
novostroika = []
for_kat = []
# Запускаем прописанный парсер
sad_parsing('https://www.avito.ru/moskva/kvartiry/prodam/novostroyka-ASgBAQICAUSSA8YQAUDmBxSOUg?cd=1&f=ASgBAQICAUSSA8YQAkDmBxSOUr7BDRSCnZQC&p=', 3)

# Объединяем все в таблицу для дальнейшего использования
# Категориальные данные заполняем вручную: парсер возвращает длину списка, умножаем ее на 0, если признак не присущ квартире, 1 - присущ. 
# Признаки нам заранее известны (каждая ссылка ведет на уникальное сочетание признаков: новостройка + окна во двор, новостройка + окна на улицу и т.д.) 

na_ul.extend([0]*for_kat[0])
vo_dvor.extend([0]*for_kat[0])
na_soln.extend([1]*for_kat[0])
novostroika.extend([1]*for_kat[0])
df = pd.DataFrame({'Тип квартиры': flat_f, 
              'м^2': m_2_f, 
              'Этаж': floor_f, 
              'Этажей в доме': floors_f, 
              'Адресс': adresses_f, 
              'Станция метро': stations_f,
              'Окна во двор': vo_dvor,  
              'Окна на улицу': na_ul,
              'Окна на солнечную сторону': na_soln,
              'Новостройка': novostroika,
              'Цена квартиры': prices_per_flat_f,
              'Цена за м^2': prices_per_m_f
              })

# Повторяем действия для каждой нужной ссылки

prices_per_m_f= []
prices_per_flat_f = []
flat_f = []
m_2_f = []
floor_f = []
floors_f = []
adresses_f = []
stations_f = []
vo_dvor = []
na_ul = []
na_soln = []
novostroika = []
for_kat = []
sad_parsing('https://www.avito.ru/moskva/kvartiry/prodam/vtorichka-ASgBAQICAUSSA8YQAUDmBxSMUg?cd=1&f=ASgBAQICAUSSA8YQAkDmBxSMUr7BDRSCnZQC&p=', 6)

na_ul.extend([0]*for_kat[0])
vo_dvor.extend([0]*for_kat[0])
na_soln.extend([1]*for_kat[0])
novostroika.extend([0]*for_kat[0])

df2 = pd.DataFrame({'Тип квартиры': flat_f, 
              'м^2': m_2_f, 
              'Этаж': floor_f, 
              'Этажей в доме': floors_f, 
              'Адресс': adresses_f, 
              'Станция метро': stations_f,
              'Окна во двор': vo_dvor,  
              'Окна на улицу': na_ul,
              'Окна на солнечную сторону': na_soln,
              'Новостройка': novostroika,
              'Цена квартиры': prices_per_flat_f,
              'Цена за м^2': prices_per_m_f
              })
df = df.append(df2, ignore_index = True )

prices_per_m_f= []
prices_per_flat_f = []
flat_f = []
m_2_f = []
floor_f = []
floors_f = []
adresses_f = []
stations_f = []
vo_dvor = []
na_ul = []
na_soln = []
novostroika = []
for_kat = []
sad_parsing('https://www.avito.ru/moskva/kvartiry/prodam/novostroyka-ASgBAQICAUSSA8YQAUDmBxSOUg?cd=1&f=ASgBAQICAUSSA8YQAkDmBxSOUr7BDRS2_Tc&p=', 11)

na_ul.extend([1]*for_kat[0])
vo_dvor.extend([0]*for_kat[0])
na_soln.extend([0]*for_kat[0])
novostroika.extend([1]*for_kat[0])

df3 = pd.DataFrame({'Тип квартиры': flat_f, 
              'м^2': m_2_f, 
              'Этаж': floor_f, 
              'Этажей в доме': floors_f, 
              'Адресс': adresses_f, 
              'Станция метро': stations_f,
              'Окна во двор': vo_dvor,  
              'Окна на улицу': na_ul,
              'Окна на солнечную сторону': na_soln,
              'Новостройка': novostroika,
              'Цена квартиры': prices_per_flat_f,
              'Цена за м^2': prices_per_m_f
              })
df = df.append(df3, ignore_index = True )


prices_per_m_f= []
prices_per_flat_f = []
flat_f = []
m_2_f = []
floor_f = []
floors_f = []
adresses_f = []
stations_f = []
vo_dvor = []
na_ul = []
na_soln = []
novostroika = []
for_kat = []
sad_parsing('https://www.avito.ru/moskva/kvartiry/prodam/novostroyka-ASgBAQICAUSSA8YQAUDmBxSOUg?cd=1&f=ASgBAQICAUSSA8YQAkDmBxSOUr7BDRS4_Tc&p=', 31)

na_ul.extend([0]*for_kat[0])
vo_dvor.extend([1]*for_kat[0])
na_soln.extend([0]*for_kat[0])
novostroika.extend([1]*for_kat[0])

df4 = pd.DataFrame({'Тип квартиры': flat_f, 
              'м^2': m_2_f, 
              'Этаж': floor_f, 
              'Этажей в доме': floors_f, 
              'Адресс': adresses_f, 
              'Станция метро': stations_f,
              'Окна во двор': vo_dvor,  
              'Окна на улицу': na_ul,
              'Окна на солнечную сторону': na_soln,
              'Новостройка': novostroika,
              'Цена квартиры': prices_per_flat_f,
              'Цена за м^2': prices_per_m_f
              })


df = df.append(df4, ignore_index = True )


prices_per_m_f= []
prices_per_flat_f = []
flat_f = []
m_2_f = []
floor_f = []
floors_f = []
adresses_f = []
stations_f = []
vo_dvor = []
na_ul = []
na_soln = []
novostroika = []
for_kat = []
sad_parsing('https://www.avito.ru/moskva/kvartiry/prodam/vtorichka-ASgBAQICAUSSA8YQAUDmBxSMUg?cd=1&f=ASgBAQICAUSSA8YQAkDmBxSMUr7BDRS4_Tc&p=', 32)

na_ul.extend([0]*for_kat[0])
vo_dvor.extend([1]*for_kat[0])
na_soln.extend([0]*for_kat[0])
novostroika.extend([0]*for_kat[0])

df5 = pd.DataFrame({'Тип квартиры': flat_f, 
              'м^2': m_2_f, 
              'Этаж': floor_f, 
              'Этажей в доме': floors_f, 
              'Адресс': adresses_f, 
              'Станция метро': stations_f,
              'Окна во двор': vo_dvor,  
              'Окна на улицу': na_ul,
              'Окна на солнечную сторону': na_soln,
              'Новостройка': novostroika,
              'Цена квартиры': prices_per_flat_f,
              'Цена за м^2': prices_per_m_f
              })
df = df.append(df5, ignore_index = True )


prices_per_m_f= []
prices_per_flat_f = []
flat_f = []
m_2_f = []
floor_f = []
floors_f = []
adresses_f = []
stations_f = []
vo_dvor = []
na_ul = []
na_soln = []
novostroika = []
for_kat = []
sad_parsing('https://www.avito.ru/moskva/kvartiry/prodam/vtorichka-ASgBAQICAUSSA8YQAUDmBxSMUg?cd=1&f=ASgBAQICAUSSA8YQAkDmBxSMUr7BDRS2_Tc', 17)


na_ul.extend([1]*for_kat[0])
vo_dvor.extend([0]*for_kat[0])
na_soln.extend([0]*for_kat[0])
novostroika.extend([0]*for_kat[0])

df6 = pd.DataFrame({'Тип квартиры': flat_f, 
              'м^2': m_2_f, 
              'Этаж': floor_f, 
              'Этажей в доме': floors_f, 
              'Адресс': adresses_f, 
              'Станция метро': stations_f,
              'Окна во двор': vo_dvor,  
              'Окна на улицу': na_ul,
              'Окна на солнечную сторону': na_soln,
              'Новостройка': novostroika,
              'Цена квартиры': prices_per_flat_f,
              'Цена за м^2': prices_per_m_f
              })
df = df.append(df6, ignore_index = True )

# Сохраняем итоговую таблицу
df.to_csv('final_table.csv') 
