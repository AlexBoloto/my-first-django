import requests
from bs4 import BeautifulSoup
import re
import csv
import time
import transliterate
title='a'

maxpage = 80
#id = 44399
def load_data(id,page):
    url = \
        'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&from_developer=1&newobject[0]=%d&offer_type=flat&p=%d'\
        % (id,page)
    r = requests.get(url)
    return r.text
def parce_page(text):
    global maxpage
    global title
    price =[]
    br =[]
    ppm = []
    results =[]
    id_flat=[]
    flat_type=[]
    sqr = []
    floor = []
    text_block =[]
    stage_of_building=[]
    soup = BeautifulSoup(text, 'lxml')
    div = soup.find_all('div', class_='c6e8ba5398-title--3WDDX')
    div_price = soup.find_all('div', class_='c6e8ba5398-header--6WXYW')
    div_price_per_meter = soup.find_all('div', class_='c6e8ba5398-term--39cia')
    div_text_block = soup.find_all('div', class_='c6e8ba5398-container--_4ZtZ c6e8ba5398-info-section--28o47')
    soup = BeautifulSoup(text, 'lxml')
    footer = soup.find_all('a', class_='_93444fe79c-list-itemLink--39icE')
    title = soup.find('div',class_='_93444fe79c-content-title--2j5Rr').text
    title = transliterate.translit(title,reversed=True)
    for i in footer:
        if i.text.isdigit():
            br.append(int(i.text))
            maxpage = max(br)
    for i in div_text_block:
        text_block.append(i.text)
    for i in div_price:
        price.append(re.sub(('\D'),'',i.text))
    for i in div:
        a = re.split(',',i.text)
        flat_type.append(a[0])
        sqr.append(re.sub(('\D'),'',a[1]))
        #floor.append(re.sub((' '),'',re.sub(('этаж'),'',a[2])))
        floor.append(a[2])
    for i in div_price_per_meter:
        ppm.append(re.sub(('\D'),'',i.text))
    for i in soup.find_all('div',class_='c6e8ba5398-info-section--28o47 c6e8ba5398-main-info--Rfnfh'):
        id_flat.append(re.sub(('\D'),'',i.find('a').get('href')))
    for i in soup.find_all('div', class_='c6e8ba5398-deadline--1eIA6'):
        stage_of_building.append(i.text)
    print(id_flat)
    for i in range(len(id_flat)):
        try:
        #if text_block[i][0:text_block[i].find(' ')] == text_block[0][0:text_block[i].find(' ')]:
            results.append({
                'id': id_flat[i],
                'Тип квартиры': flat_type[i],
                'Площадь': sqr[i],
                'Этаж': floor[i],
                'Цена': price[i],
                'Цена за метр': ppm[i],
                'Статус': stage_of_building[i],
                'Описание': text_block[i]
               })
        except IndexError:
            continue
    #print(results[i])
    return results
def write_csv(lst):
    with open(title + '.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file,delimiter =";",fieldnames=["id", "Тип квартиры", "Площадь", "Этаж", "Цена", "Цена за метр", "Статус", "Описание"])
        writer.writeheader()
        writer.writerows(lst)
def add_csv(lst):
    with open(title + '.csv', 'a', newline='') as csv_file:
        adder = csv.DictWriter(csv_file,delimiter =";", fieldnames=["id", "Тип квартиры", "Площадь", "Этаж", "Цена", "Цена за метр", "Статус", "Описание"])
        adder.writerows(lst)
def main(id):
    cp=1
   # maxpage=80
    #id = 44399

    while(cp<=maxpage):
        res = parce_page(load_data(id,cp))
        print(cp, maxpage)
        if cp == 1:
            write_csv(res)
        else:
            add_csv(res)
        cp += 1
        time.sleep(5)
if __name__ == '__main__':
    main()