import requests
from bs4 import BeautifulSoup
from matplotlib.pyplot import title

if __name__ == '__main__':
    title='_'
    brand='_'
    price='_'
    fetures='_'
    all_features=[]
    record=[]
    #Access the page
    r = requests.get('https://www.daraz.com.np/karbonn-polymer-10-10000mah-power-bank-black-49035.html')
    if r.status_code==200:
        html=r.text
        soup=BeautifulSoup(html,'lxml')
        #title
        title_section=soup.find('h1')
        if title_section:
            title=title_section.text


        #Brand
        brand_section=soup.select('.sub-title > a')
        if brand_section:
            brand=brand_section[0].text


        #features
        features_section=soup.select('.list ul > li')
        if features_section:
            for f in features_section:
                all_features.append(f.text)

            features='|'.join(all_features)  #using delimintar with pipe'|'



        #price
        price_section=soup.select('.price > span')
        if price_section and len(price_section)> 1:
            price =price_section[1].text.replace(',', '').strip()


        record.append(title)
        record.append(brand)
        record.append(price)
        record.append(features)


        #store data in CSV
        with open('result_data1.csv','a+', encoding='utf-8') as file:
            file.write('Title,Brand,price,features\n')
            file.write(','.join(record))


