
def getObject():
    new_path = 'tmpObject.html'
    return open(new_path, mode='r', encoding="utf-8").read()


def getPrice(content):
    price = 'sold-property__price-value'

    start_index = content.find(price) + len(price) + 2
    content1 = content[start_index:]
    end_index = content1.find('kr')
    content2 = content1[0:end_index]
    content3 = content2.replace(u'\xa0', '')
    return int(content3)

def getGetKvm(content):
    kvm = 'sold-property__attribute-value'
#page-content > div.column.large > div.sold-property > div.sold-property__details > dl.sold-property__attributes > dd:nth-child(4)
content = getObject()

price = getPrice(content)

print(price)
print("done")
