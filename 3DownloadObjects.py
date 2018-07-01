import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
new_path = 'soldObjectsUrls.csv'
features = ''
content = ''
with open(new_path, mode='r', encoding="utf-8") as fin:
    for line in fin:
        response = requests.get(line, headers=headers)
        content = response.text
        break

new_path = 'tmpObject.html'
new_days = open(new_path, mode='w', encoding="utf-8")
new_days.write(content)
print("done")

