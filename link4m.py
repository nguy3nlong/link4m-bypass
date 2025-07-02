import requests
import re
import time
type = input('type: ')
if type == 'soikeo':
    url = 'https://soikeo.uk.com/'
    key = 'u0cLg'
    path = '/'
    hostname = url
if type == 'xosodientu':
    url = 'https://xosodientu.com/'
    key = 'sdgQhQny'
    path = '/'
    hostname = url
if type == 'hutbephotvietphat':
    url = 'https://hutbephotvietphat.vn/hut-be-phot-tai-hoa-binh-uy-tin-gia-re-0947-888-198-bid21.html'
    key = 'U8022T1'
    path = '/hut-be-phot-tai-hoa-binh-uy-tin-gia-re-0947-888-198-bid21.html'
    hostname = 'https://hutbephotvietphat.vn'

if type == '79king':
    url = 'https://fitting.us.com/'
    key = 'gLaiBZ'
    path = '/'
    hostname = url

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': hostname,
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
}

params = {
    'key': key,
}

response = requests.get('https://s1.what-on.com/widget/service.js', params=params, headers=headers)
if response.status_code == 200:
    js = response.text

    pattern = r'var\s+(\w+)\s*=\s*(["\'])(.*?)\2\s*;'
    matches = re.findall(pattern, js)

    def decode(s):
        return bytes(s, "utf-8").decode("unicode_escape")

    
    traffic_key = traffic_id = traffic_domain = traffic_session = uuid_name = None

    for name, _, value in matches:
        if name == "traffic_key":
            traffic_key = decode(value)
        elif name == "traffic_id":
            traffic_id = decode(value)
        elif name == "traffic_domain":
            traffic_domain = decode(value)
        elif name == "traffic_session":
            traffic_session = decode(value)
        elif name == "uuid_name":
            uuid_name = decode(value)
    print('Please wait 90 seconds')
    time.sleep(90)
    params = {
    'code': traffic_id,
    'traffic_session': traffic_session,
    'screen': '1000 x 1000',
    'browser': 'Skibidi',
    'browserVersion': '100',
    'browserMajorVersion': '100',
    'mobile': 'false',
    'os': 'SkibidiOS',
    'osVersion': '5',
    'cookies': 'true',
    'flashVersion': 'no check',
    'lang': 'en-US',
    'client_id': traffic_session,
    'pathname': path,
    'href': url,
    'hostname': hostname,
}
    aresponse = requests.get('https://s1.what-on.com/widget/get_code.html', params=params, headers=headers)
    if aresponse.status_code == 200:
        print(aresponse.json())
    else:
        print('fail shit')
    

    

else:
    raise RuntimeError("cannot load the shit js or request failed")
