import requests

noMoreHits = 'Inga träffar på slutpriser'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
result = ''
content = ''
page = 1
while not content.__contains__(noMoreHits) and page < 200:
    result = result + content
    path = f'https://www.hemnet.se/salda/bostader?item_types%5B%5D=bostadsratt&location_ids%5B%5D=898472&page={page}&sold_age=6m'
    response = requests.get(path, headers=headers)
    content = response.text
    page = page + 1

new_path = 'HemnetSearchResults2.html'
new_days = open(new_path, mode='w', encoding='utf-8')
new_days.write(result)

print("done")
