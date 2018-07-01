from bs4 import BeautifulSoup

new_path = 'tmpObject.html'
doc = open(new_path, mode='r', encoding="utf-8").read()

soup = BeautifulSoup(doc, 'html.parser')

property_details = soup.find_all("div", class_='sold-property__details')[0]

# for child in find_all.children:
#     print(child)
# print(property_details)
rooms = property_details.find_all('dd')
for child in rooms:
    # if child.previous_sibling:
    #     print(child.previous_sibling.text)
    print(child.text)
# print(rooms)

print('done')