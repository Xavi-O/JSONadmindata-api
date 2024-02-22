import multiprocessing
import json, requests, pytz, schedule, time
from os import path
from bs4 import BeautifulSoup
from datetime import datetime
from multiprocessing import Process

currentdatetime = datetime.now(pytz.timezone('Africa/Nairobi'))

menus = ['Fresh-Black-Seedless-Grapes-500G',
'Isinya-Eggs-15-S',
'Green-Farm-Yellow-Yolk-Egg-30-Pieces-Wrapped',
'Nutrameal-Packed-Sugar-White-2Kg',
'Naivas-Premium-Toilet-Tissue-2-Ply-10-Rolls',
'Isinya-Eggs-30-Pieces',
'Fresh-Tangerines-Imported-1Kg-(Pre-pack)',
'Keringet-Mineral-Water-10L',
'Naivas-Beef-Meat-On-Bone-P/Kg',
'Isinya-Eggs-15-Pieces',
"Farmer's-Choice-Safari-Beef-Sausages-500G",
'Aquamist-Mineral-Water-10-Ltr',
'Coke-Assorted-Soda-Pre-Pack-4*-2Lt-Pet',
"Farmer's-Choice-Beef-Sausagess-Value-Pack-1Kg",
'Economy-White-Sugar-2-Kg',
"Farmer's-Choice-Streaky-Bacon-200Gm",
'Fresha-Whole-Milk-5Ltr',
"Farmer's-Choice-Pork-Sausages-Value-Pack-1Kg",
'Velvex-Kitchen-Towel-2-Rolls',
'Blueband-Margarine-1Kg',
'Naivas-Local-Sugar-White-2Kg',
'Fresh-Green-Peas-500G',
'Zesta-Tomato-Sauce-5L',
'Celine-Toilet-Tissue-10-Pack',
'Naivas-Beef-Rump-Steak',
'Naivas-Beef-Ossubucco-P/Kg',
'Toilex-White-Tissue-Paper-10-Unwrapped']

##Glovo delivery addresses delivery cookies
"""NBO Addresses"""
capitalcenter = '{"geo":{"lat":-1.3166543,"lng":36.8345953},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJh-tZma8RLxgRXoQelRHB_ms","text":"Mombasa Road"}'
ciatamall = '{"geo":{"lat":-1.2260145,"lng":36.8383813},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJIZiy4ToWLxgR2PqoRfR32Qk","text":"Kiambu Road"}'
freedomheightsmall = '{"geo":{"lat":-1.3209053,"lng":36.8020882},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJY4vVOq8aLxgRp2G4EwGsn84","text":"Langata Road"}'
thepointmall = '{"geo":{"lat":-1.2941946,"lng":36.8759487},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJdchPfucTLxgRi-p2qCwxyQI","text":"Rabai Road"}'
donholm = '{"geo":{"lat":-1.2969393,"lng":36.886881},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJl8DmH8ETLxgRSspE59JgX1o","text":"Donholm Naivas"}'
prestigemall = '{"geo":{"lat":-1.3004076,"lng":36.7870774},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJY6i0nMYRLxgRsd4gJVAbCl4","text":"Ngong Road Prestige Plaza Shopping Mall, Nairobi, Kenya"}'
themallwestlands = '{"geo":{"lat":-1.2643982,"lng":36.80279549999999},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJ27DxHkAXLxgRAPV1CJpDC8w","text":"Ring Road Parklands"}'
mountainmall = '{"geo":{"lat":-1.232878,"lng":36.8736272},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJl4so_d0VLxgRvnP-qXGcn28","text":"Ground Floor, Mountain Mall, Nairobi, Kenya"}'
kasarani = '{"geo":{"lat":-1.2591043,"lng":36.8265395},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJH4t-WPkiLxgRSfI48do1KGI","text":"Limuru Road"}'
kilimanimall = '{"geo":{"lat":-1.224386,"lng":36.913781},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJj-pPkHYVLxgRbFWGyi3j5g4","text":"Kasarani Mwiki Road"}'
hazinatradecenter = '{"geo":{"lat":-1.2817329,"lng":36.8183403},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJS-RtV9QRLxgR-ix0liYijnY","text":"Monrovia Street"}'
imaaramall = '{"geo":{"lat":-1.328015,"lng":36.8814316},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJgavTZEUTLxgRSNB0TStkHQk","text":"Embakasi, Nairobi, Kenya"}'
reyhanstation = '{"geo":{"lat":-1.2829946,"lng":36.7368728},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJ_edbHNUbLxgRy6Q_JlywvNo","text":"Naivasha Road"}'
greenspanmall = '{"geo":{"lat":-1.2895871,"lng":36.9009077},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJjYJ4cZoTLxgRUAPj8Z0zRCs","text":"Savannah Road"}'
northparkmall = '{"geo":{"lat":-1.1690783,"lng":36.9697903},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJ7SUn5q1BLxgR5NSIbYlE4ho","text":"Kamakis, Ruiru, Kenya"}'
spurmall = '{"geo":{"lat":-1.1364395,"lng":36.9703024},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJ_4mT-YFHLxgRC5xZMP7bcFQ","text":"Ruiru, Kenya"}'
lavingtoncurvemall = '{"geo":{"lat":-1.2782808,"lng":36.7694457},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJM3hR1_YZLxgRijsh4PhmbVY","text":"Naushad Merali Drive"}'
broadwalkmall = '{"geo":{"lat":-1.2707124,"lng":36.8132104},"city":{"code":"NBO","name":"Nairobi","countryCode":"KE"},"placeId":"ChIJ9V3fw5MXLxgRakAXPgPfQt0","text":"Broadwalk Mall"}'

"""NAK Addresses"""
kenyattaavenue = '{"geo":{"lat":-0.2871079,"lng":36.0638217},"city":{"code":"NAK","name":"Nakuru","countryCode":"KE"},"placeId":"ChIJ8xi-ZsWNKRgRdGEGbpYArP8","text":"Kenyatta Avenue"}'
supercenter = '{"geo":{"lat":-0.2830922,"lng":36.0892349},"city":{"code":"NAK","name":"Nakuru","countryCode":"KE"},"placeId":"ChIJ2Ye54YmNKRgRTRW_hSt1rRA","text":"naivas mall along Nakuru Nairobi highway, Nakuru, Kenya"}'

"""MBS Addresses"""
nyalicenter = '{"geo":{"lat":-4.022099,"lng":39.7195893},"city":{"code":"MBS","name":"Mombasa","countryCode":"KE"},"placeId":"ChIJR0cYmfYNQBgRVFhASzg4Sm0","text":"Links Road, XPH9+5R8, Nyali Centre, Mombasa, Kenya"}'
mwembetayari = '{"geo":{"lat":-4.057011,"lng":39.6697158},"city":{"code":"MBS","name":"Mombasa","countryCode":"KE"},"placeId":"ChIJk7DGnRATQBgReRoebjAUYOE","text":"Mwembe Tayari Road"}'
likonimall = '{"geo":{"lat":-4.0745673,"lng":39.6659332},"city":{"code":"MBS","name":"Mombasa","countryCode":"KE"},"placeId":"ChIJP4aTP90TQBgR912XGCNGN5A","text":"Nyerere Avenue"}'
bamburi = '{"geo":{"lat":-4.0024525,"lng":39.7012891},"city":{"code":"MBS","name":"Mombasa","countryCode":"KE"},"placeId":"ChIJ159vTo8NQBgRxblUfaPtDfU","text":"Bamburi, Mombasa, Kenya"}'

"""NRK Addresses"""
ngonghomeground = '{"geo":{"lat":-1.3419946,"lng":36.6662846},"city":{"code":"NRK","name":"Ngong - Rongai - Karen","countryCode":"KE"},"placeId":"ChIJE3javSsdLxgRLpOGQI2y0-4","text":"Ngong Road, Ngong, Kenya"}'
waterfront = '{"geo":{"lat":-1.3297271,"lng":36.7148028},"city":{"code":"NRK","name":"Ngong - Rongai - Karen","countryCode":"KE"},"placeId":"ChIJfX9mCVcbLxgR3mGNANwpsOQ","text":"Karen Road"}'
ongatarongai = '{"geo":{"lat":-1.3938406,"lng":36.7441953},"city":{"code":"NRK","name":"Ngong - Rongai - Karen","countryCode":"KE"},"placeId":"ChIJ-VqjDLMFLxgRaL59EU0XUok","text":"Ongata Rongai, Kenya"}'

"""ELD Addresses"""
nandiroad = '{"geo":{"lat":0.5142916,"lng":35.2773833},"city":{"code":"ELD","name":"Eldoret","countryCode":"KE"},"placeId":"ChIJX-qRMqMBgRcRgUU6RzJU_EE","text":"Nandi Road"}'
zionmall = '{"geo":{"lat":0.5176658,"lng":35.278194},"city":{"code":"ELD","name":"Eldoret","countryCode":"KE"},"placeId":"ChIJERsUeNsBgRcRXVFdxGWZBvc","text":"Sigot, Kenya"}'
elgonviewmall = '{"geo":{"lat":0.5014741,"lng":35.2708475},"city":{"code":"ELD","name":"Eldoret","countryCode":"KE"},"placeId":"ChIJ97xiCuoBgRcRm_it1fvsnow","text":"Kisumu Road, Eldoret, Kenya"}'

"""KSM Addresses"""
achiengoneko = '{"geo":{"lat":-0.1026497,"lng":34.7565835},"city":{"code":"KSM","name":"Kisumu","countryCode":"KE"},"placeId":"ChIJ9ZPP6ZOkKhgRI4lvn9a8_m0","text":"Achieng\' Oneko Road"}'
megacitymall = '{"geo":{"lat":-0.1069111,"lng":34.7704177},"city":{"code":"KSM","name":"Kisumu","countryCode":"KE"},"placeId":"ChIJ4_VmG0GlKhgRpUm1LjfR3XU","text":"Mega City Mall, Kisumu, Kenya"}'
kisumusimba = '{"geo":{"lat":-0.0991875,"lng":34.7619375},"city":{"code":"KSM","name":"Kisumu","countryCode":"KE"},"placeId":"ChIJ-2oEZxqlKhgRiNpFaHa2mpg","text":"Northern"}'

"""THK Addresses"""
ananasmall = '{"geo":{"lat":-1.0557004,"lng":37.1139475},"city":{"code":"THK","name":"Thika","countryCode":"KE"},"placeId":"ChIJhzFqFjJOLxgROK9FoJdr53g","text":"Ananas mall, makongeni, Garissa Rd, Thika, Kenya"}'
workshoplane = '{"geo":{"lat":-1.0364178,"lng":37.0727075},"city":{"code":"THK","name":"Thika","countryCode":"KE"},"placeId":"ChIJF8cD-Y9OLxgR5JS9fC0FEoA","text":"Workshop Lane"}'

"""SYO Addresses"""
gatewaymall = '{"geo":{"lat":-1.3921923,"lng":36.9407301},"city":{"code":"SYO","name":"Syokimau","countryCode":"KE"},"placeId":"ChIJbWMb4VsNLxgR0aWbOFtDkQw","text":"Syokimau/Mulolongo, Mombasa, Kenya"}'
kitengelamall = '{"geo":{"lat":-1.479082,"lng":36.9583793},"city":{"code":"SYO","name":"Syokimau","countryCode":"KE"},"placeId":"ChIJsx58USqfLxgRzr35JSBIEjE","text":"Nairobi - Namanga"}'
katani = '{"geo":{"lat":-1.3741457,"lng":36.9230499},"city":{"code":"SYO","name":"Syokimau","countryCode":"KE"},"placeId":"ChIJPx0E7lkNLxgRs5I8b4Ubvu0","text":"Mombasa Road"}'

"""DIA Addresses"""
gatemallukunda = '{"geo":{"lat":-4.2807655,"lng":39.5661889},"city":{"code":"DIA","name":"Diani","countryCode":"KE"},"placeId":"ChIJmdXe1eNFQBgR6MUn4DDCSsc","text":"Ukunda-Ramisi Road"}'

products = []
filename = 'naivas-products.json'

cities = {
    'NBO': ['https://glovoapp.com/ke/en/nairobi/naivas-nbo?search='],
    'NAK': ['https://glovoapp.com/ke/en/nakuru/naivas-nak?search='],
    'MBS': ['https://glovoapp.com/ke/en/mombasa/naivas-mbs?search='],
    'NRK': ['https://glovoapp.com/ke/en/ngong-rongai-karen/naivas-nrk?search='],
    'ELD': ['https://glovoapp.com/ke/en/eldoret/naivas-eld?search='],
    'KSM': ['https://glovoapp.com/ke/en/kisumu/naivas-ksm?search='],
    'THK': ['https://glovoapp.com/ke/en/thika/naivas-ananas-mall-thk/?search='],
    'SYO': ['https://glovoapp.com/ke/en/syokimau/naivas-syo?search='],
    'DIA': ['https://glovoapp.com/ke/en/diani/naivas-dia?search='],
}

locations = {
    'NBO': [capitalcenter, ciatamall, freedomheightsmall, thepointmall, donholm, prestigemall, themallwestlands, 
            mountainmall, kasarani, kilimanimall, hazinatradecenter, imaaramall, reyhanstation, greenspanmall, 
            northparkmall,spurmall, lavingtoncurvemall, broadwalkmall],
    'NAK': [kenyattaavenue, supercenter],
    'MBS': [nyalicenter, mwembetayari, likonimall, bamburi],
    'NRK': [ngonghomeground, waterfront, ongatarongai],
    'ELD': [nandiroad, zionmall, elgonviewmall],
    'KSM': [achiengoneko, megacitymall, kisumusimba],
    'THK': [ananasmall, workshoplane],
    'SYO': [gatewaymall, kitengelamall, katani],
    'DIA': [gatemallukunda],
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
    #print(products)
    

if __name__ == "__main__":
    def naivas_job():
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

schedule.every().day.at('09:00').do(naivas_job)
schedule.every().day.at('13:00').do(naivas_job)
schedule.every().day.at('15:00').do(naivas_job)
schedule.every().day.at('18:10').do(naivas_job)

while True:
    schedule.run_pending()
    time.sleep(1)