from bs4 import BeautifulSoup

new_path = 'C:/git/bostadml/tmpObject.html'
doc = open(new_path, mode='r', encoding="utf-8").read()

soup = BeautifulSoup(doc, 'html.parser')

find_all = soup.find_all("div", class_='sold-property__details')[0]

# for child in find_all.children:
#     print(child)
print(find_all)
rooms = find_all.find_all('dt', class_='sold-property__attribute-value')
print(rooms)

print('done')