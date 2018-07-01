import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
path = 'soldObjectsUrls.csv'
features = ''
content = ''

with open(path, mode='r', encoding="utf-8") as fin:
    index = 0
    for line in fin:
        response = requests.get(line, headers=headers)
        content = response.text
        path = f'objects/object${index}.html'
        new_days = open(path, mode='w', encoding="utf-8")
        new_days.write(content)
        index = index + 1


print("done")

