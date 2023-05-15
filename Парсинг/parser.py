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
   

