from urllib.parse import urlparse, parse_qs
# address = 'https://skyhealth-api.oucare.com/clients/kjump/users'
address = 'https://www.google.com/search?q=gray+squirrel&tbm=isch'
parts = urlparse(address)
print(parts, end='\n')
queryTest = 'texture=fuzzy&animal=gray+squirrel'
print(parse_qs(queryTest), end='\n')