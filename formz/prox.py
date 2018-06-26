import requests
from bs4 import BeautifulSoup
import re
import itertools

def load_data():
    url = 'https://www.ip-adress.com/proxy-list'
    r = requests.get(url)
    return r.text
def proxxx(text):
    ip=[]
    tp=[]
    ip_new=[]
    soup = BeautifulSoup(text, 'lxml')
    table = soup.find('table', class_="htable proxylist")
    a = table.find_all('a')
    td = table.find_all('td')
    for i in a:
        ip.append(i.text)
    for i in range(len(td)):
        if (re.findall(r':\d{2,5}',str(td[i].text))):
            tp.append(re.findall(r':\d{2,5}',str(td[i].text)))
        else:
            continue
    port_merged = list(itertools.chain(*tp))
    for i in range(len(ip)):
        ip_new.append(str(ip[i])+str(port_merged[i]))
    print(ip_new)
    for proxy in ip_new:
        url = 'http://' + proxy
        try:
            r=requests.get('http://ya.ru',proxies={'http':url})
            if r.status_code == 200:
                return url
        except requests.exceptions.ConnectionError:
            continue
def main():
    proxy = proxxx(load_data())
    print(proxy)
if __name__ == '__main__':
    main()
