import requests

def scrape_proxies():
    url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
    response = requests.get(url)
    proxies = response.text.strip().split('\r\n')
    return proxies

proxies = scrape_proxies()

with open('proxy.txt', 'w') as f:
    for proxy in proxies:
        f.write(f'{proxy}\n')
print("added proxies!")
