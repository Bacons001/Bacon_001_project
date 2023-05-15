#!/usr/bin/env python
# coding: utf-8

# In[1008]:


from bs4 import BeautifulSoup  
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
import pandas as pd

driver = webdriver.Chrome(options=options)


# In[983]:


def sad_parsing(url, num):
    for num in [*range(num)]:
        driver.get(url + str(num +2))

        price_n = driver.find_elements(By.CLASS_NAME, 'price-root-RA1pj')
        prices = [i.text.split('\n') for i in price_n]
        prices_per_m = [prices[i][1] for i in range(len(prices))]
        prices_per_flat = [prices[i][0] for i in range(len(prices))]

        prices_per_m_f.extend(prices_per_m)
        prices_per_flat_f.extend(prices_per_flat)


        title = driver.find_elements(By.CLASS_NAME, "title-root-zZCwT")
        titles = [i.text.split(', ') for i in title][::2]
        flat = [titles[i][0] for i in range(len(titles))]
        m_2 = [titles[i][1] for i in range(len(titles))]
        floor = [titles[i][2].split('/')[0] for i in range(len(prices))]
        floors = [titles[i][2].split('/')[1] for i in range(len(prices))]

        flat_f.extend(flat)
        m_2_f.extend(m_2)    
        floor_f.extend(floor)
        floors_f.extend(floors)  

        adress = driver.find_elements(By.CLASS_NAME, "geo-root-zPwRk")
        adresses = [i.text for i in adress]

        adress = [i.split('\n') for i in adresses]
        for i in range(len(adress)):
            adress[i].append('?') 

        adress_ul = [adress[i][0] for i in range(len(adress))]
        metros = [adress[i][1] for i in range(len(adress))]

        stations = []
        metro_t = []

        for i in range(len(metros)):
                lst = list(metros[i])
                station = []
                metro = []
                for i in lst:
                    if i == '?':
                        stations.append('')
                        metro_t.append('')

                    elif i.isalpha() or i == ' ':
                        station.append(i)

                if i != '?':
                    new_words = []
                    words = ''.join(station).split(' ')
                    words = list(filter(None, words))
                    if words[-1] == 'мин':
                        lst = list(words[:-1])
                    else:
                        lst = list(words)
                    new_words.extend(lst)

                    copy = new_words.copy()
                    copy = list(' '.join(copy))
                    copy.reverse()

                    if copy[:2] == ['о', 'д'] or copy[:2] == ['т', 'о']:
                        copy.reverse()
                        lst = list(''.join(copy))[:-2]
                    else:
                        copy.reverse()
                        lst = list(''.join(copy))

                    stations.append(''.join(lst))

        adresses_f.extend(adress_ul) 
        stations_f.extend(stations)

    for_kat.append(len(stations_f))


# In[984]:


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
sad_parsing('https://www.avito.ru/moskva/kvartiry/prodam/novostroyka-ASgBAQICAUSSA8YQAUDmBxSOUg?cd=1&f=ASgBAQICAUSSA8YQAkDmBxSOUr7BDRSCnZQC&p=', 3)


# In[989]:


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
df.head()


# In[990]:


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


# In[997]:


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


# In[999]:


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


# In[1000]:


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


# In[1003]:


df = df.append(df3, ignore_index = True )


# In[1009]:


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


# In[1010]:


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


# In[1020]:


df = df.append(df4, ignore_index = True )


# In[1011]:


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


# In[1012]:


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


# In[1018]:


df = df.append(df5, ignore_index = True )


# In[1013]:


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


# In[1014]:


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


# In[1022]:


df = df.append(df6, ignore_index = True )


# In[1024]:


df.head()


# In[1026]:


df.to_csv('final_table.csv') 

