import multiprocessing
import json, requests, pytz, schedule, time
from os import path
from bs4 import BeautifulSoup
from datetime import datetime
from multiprocessing import Process

currentdatetime = datetime.now(pytz.timezone('Africa/Nairobi'))

    
#Glovo delivery addresses delivery cookies
"""NBO Addresses"""
hurlingham = '{"geo":{"lat":-1.2954666,"lng":36.7994376},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJRQUQ9ZUQLxgRyGDzL6j-x4c","text":"Shell Hurlingham"}'
junctionmall = '{"geo":{"lat":-1.2974947,"lng":36.7616236},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJx-9eV3kbLxgRMQz48X4Ew1o","text":"Ngong Road"}'
langata = '{"geo":{"lat":-1.3228596,"lng":36.8020584},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJVRfJul4RLxgRN8YgwGptFVg","text":"Langata Road"}'
lavington = '{"geo":{"lat":-1.2791793,"lng":36.7706398},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJEXibyKIZLxgRtTEFdmPolFQ","text":"Ndoto Road"}'
imaradaima = '{"geo":{"lat":-1.3257499,"lng":36.8500653},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJ68VU-l0RLxgRq4fdVF0bXWs","text":"Imara Daima - Mombasa Rd"}'
woodvalegroove = '{"geo":{"lat":-1.2630186,"lng":36.8034397},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJmUt9zWoXLxgRvY0rja9MwIk","text":"Woodvale Grove"}'
buruburu = '{"geo":{"lat":-1.2866156,"lng":36.8808219},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJa3FWa98RLxgR9r7HHaQs7ME","text":"Mumias South Road"}'
waiyakiway = '{"geo":{"lat":-1.2586731,"lng":36.7814697},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJqYjXf0UZLxgRzlL4JonyD-0","text":"Waiyaki Way"}'
limururoad = '{"geo":{"lat":-1.2591043,"lng":36.8265395},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJH4t-WPkiLxgRSfI48do1KGI","text":"Limuru Road"}'
kasarani = '{"geo":{"lat":-1.224386,"lng":36.913781},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJj-pPkHYVLxgRbFWGyi3j5g4","text":"Kasarani Mwiki Road"}'
kiamburoad = '{"geo":{"lat":-1.2113039,"lng":36.8329204},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJgTB32Rk9LxgRoIMkxXf8pq0","text":"Kiambu Road"}'
eastleigh = '{"geo":{"lat":-1.2795907,"lng":36.84903329999999},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJidZ_ZMURLxgRea0nv31YBuA","text":"Timboroa Street"}'
kimathistreet = '{"geo":{"lat":-1.2837414,"lng":36.8227456},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJ8Zc51tUQLxgRqyEWWQhegvs","text":"Kimathi Street"}'
southfieldmall = '{"geo":{"lat":-1.3285167,"lng":36.8904553},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJM-UJumwSLxgRpztTBGDjMck","text":"Eastern Bypass"}'
gardencity = '{"geo":{"lat":-1.2329814,"lng":36.8788826},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJuYRFrMIVLxgRXguk27x3aqc","text":"Roysambu Thika Rd Garden City Mall Roysambu, Nairobi, Kenya"}'
embakasi = '{"geo":{"lat":-1.3177959,"lng":36.91789869999999},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJ2WYzU_kTLxgRcN3_MNhF4dE","text":"Airport North Road"}'
villagemarket = '{"geo":{"lat":-1.2293591,"lng":36.8048235},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJ62AMLMAXLxgRbPtWbAUV6as","text":"Village Market, Nairobi, Kenya"}'
westgate = '{"geo":{"lat":-1.2573822,"lng":36.8032038},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJSaUMeqMXLxgRmaxASGDCrpo","text":"Mwanzi Road"}'
northview = '{"geo":{"lat":-1.2496586,"lng":36.8609906},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJOekzHIcWLxgR6RcmByR1OCg","text":"Kenya Pipeline, Nairobi, Kenya"}'
mamangina = '{"geo":{"lat":-1.2855734,"lng":36.8233027},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJ2SAXs9cQLxgRJCFLOYVh6xI","text":"Mama Ngina Street"}'

"""NRK Addresses"""
thehubkaren = '{"geo":{"lat":-1.3203547,"lng":36.704113},"city":{"code":"NRK","name":"Ngong - Rongai - Karen","countryCode":"KE"},"placeId":"ChIJI6wJ4nobLxgR7YmvPaFolek","text":"Dagoretti Road"}'
maiyanmall = '{"geo":{"lat":-1.3969662,"lng":36.7619078},"city":{"code":"NRK","name":"Ngong - Rongai - Karen","countryCode":"KE"},"placeId":"ChIJZf6CZGcFLxgR5BAYjnlCXl4","text":"Magadi Road"}'
galleriamall = '{"geo":{"lat":-1.3434791,"lng":36.76597539999999},"city":{"code":"NRK","name":"Ngong - Rongai - Karen","countryCode":"KE"},"placeId":"ChIJOWZuRUsFLxgRJ6niE176d6g","text":"Langata Road"}'

"""MBS Addresses"""
mombasacbd = '{"geo":{"lat":-4.063759999999999,"lng":39.67232810000001},"city":{"code":"MBS","name":"Mombasa","countryCode":"KE"},"placeId":"ChIJxRAX2igTQBgRt8XUU7-0gvQ","text":"Trade Centre"}'
nyali = '{"geo":{"lat":-4.0300646,"lng":39.6917328},"city":{"code":"MBS","name":"Mombasa","countryCode":"KE"},"placeId":"ChIJ_0uDRHwSQBgRlz_OeI7PN3I","text":"Nyali Road"}'

"""NAK Addresses"""
westendmall = '{"geo":{"lat":-0.287257,"lng":36.0639156},"city":{"code":"NAK","name":"Nakuru","countryCode":"KE"},"placeId":"ChIJG6qqaL-NKRgRPxJLIKX_b4U","text":"West Road"}'
nakuruhyrax = '{"geo":{"lat":-0.282247,"lng":36.0945343},"city":{"code":"NAK","name":"Nakuru","countryCode":"KE"},"placeId":"ChIJp86Sk7iTKRgRUqZZtWSH6eU","text":"Nyeri-Nyahururu Road"}'

"""ELD Addresses"""
rupasmall = '{"geo":{"lat":0.5134434999999999,"lng":35.290741},"city":{"code":"ELD","name":"Eldoret","countryCode":"KE"},"placeId":"ChIJ03ropJoBgRcRe3YRf8Feaj8","text":"Rupa place"}'
    
"""KSM Addresses"""
kisumumall = '{"geo":{"lat":-0.09801349999999999,"lng":34.7622829},"city":{"code":"KSM","name":"Kisumu","countryCode":"KE"},"placeId":"ChIJQYF-24-kKhgRMwENGMZRk5I","text":"Gumbi Road"}'

"""THK Addresses"""
thikatown = '{"geo":{"lat":-1.0417845,"lng":37.0718281},"city":{"code":"THK","name":"Thika","countryCode":"KE"},"placeId":"ChIJy89ejHdPLxgRPWemWupF83Y","text":"Kenyatta Highway"}'

products = []
filename = 'kfc-products.json'
menus = ['Rice-Bliss', 'Streetwise-2', 'Streetwise-3', 'Streetwise-5', 'Streetwise-7', 'KFC-Krusher', 'Double-Crunch-Burger']

cities = {
    'NBO': ['https://glovoapp.com/ke/en/nairobi/kfc-nbo?search='],
    'NRK': ['https://glovoapp.com/ke/en/ngong-rongai-karen/kfc-nrk?search='],
    'MBS': ['https://glovoapp.com/ke/en/mombasa/kfc-mombasa?search='],
    'NAK': ['https://glovoapp.com/ke/en/nakuru/kfc-nakuru-nak-ke?search='],
    'ELD': ['https://glovoapp.com/ke/en/eldoret/kfc-eld?search='],
    'KSM': ['https://glovoapp.com/ke/en/kisumu/kfc-ksm?search='],
    'THK': ['https://glovoapp.com/ke/en/thika/kfc-thika-thk?search='],
}
locations = {
    'NBO': [hurlingham, junctionmall, langata, lavington, imaradaima, woodvalegroove, buruburu, waiyakiway,
            limururoad, kasarani, kiamburoad, eastleigh, kimathistreet, southfieldmall, embakasi, villagemarket,
            westgate, northview, mamangina],
    'NRK': [thehubkaren, maiyanmall, galleriamall],
    'MBS': [mombasacbd, nyali],
    'NAK': [westendmall, nakuruhyrax],
    'ELD': [rupasmall],
    'KSM': [kisumumall],
    'THK': [thikatown],
}

def process_menu(city, url, location, menu):
    # You can use the url here to perform the task specific to the city
    session = requests.Session()
    jar = requests.cookies.RequestsCookieJar()
    jar.set('glovo_delivery_address', location)
    session.cookies = jar
    response = session.get(url + menu)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        item = soup.find('div', class_='product-row__name').text.strip()
    except:
        item = menu
    
    price = "-" if (item == menu) else soup.find('span', class_='product-price__effective--new-card').text.strip()
    location = (location[location.rfind(':'):]).replace('"}', '').replace(':"', '')
    try:
        promo = "none" if price == "-" else (soup.find('div', class_='promotions-wrapper product-row__info__promotion').text.strip())
    except:
        promo = "none"
    return({
            'city': city, 
            'date': currentdatetime.strftime("%b %d, %Y"), 
            'time': currentdatetime.strftime("%H:00"), 
            'product': item, 
            'price': price, 
            'address': location, 
            'status': "unavailable" if price == "-" else "available", 
            'promo': promo
            })
    

if __name__ == "__main__":
    def kfc_job():
        if path.isfile(filename) is False:
            raise Exception("File not found")
        with open(filename) as fp:
            products = json.load(fp)
        with multiprocessing.Pool() as pool:
            for city, city_urls in cities.items():
                for url in city_urls:
                    for location in locations[city]:
                        results = pool.starmap(process_menu, [(city, url, location, menu) for menu in menus])
                        products.extend(results)

        with open(filename, 'w') as json_file: json.dump(products, json_file)

schedule.every().day.at('09:00').do(kfc_job)
schedule.every().day.at('13:00').do(kfc_job)
schedule.every().day.at('15:00').do(kfc_job)
schedule.every().day.at('18:00').do(kfc_job)

while True:
    schedule.run_pending()
    time.sleep(1)