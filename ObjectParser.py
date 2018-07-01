from bs4 import BeautifulSoup


def int_try_parse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


def parse(doc):
    soup = BeautifulSoup(doc, 'html.parser')

    property_details = soup.find_all("div", class_='sold-property__details')[0]

    html_values = property_details.find_all('dd')
    kvm_price = -1
    rooms = -1
    rent = -1
    running_costs = -1
    kvm = -1
    build_year = -1
    price = -1
    for child in html_values:
        text = child.text

        (numeric_value, is_numeric) = int_try_parse(text)

        if is_numeric:
            build_year = numeric_value
        elif '+' in text:
            pass
        elif '-' in text:
            pass
        elif 'brf' in text.lower():
            pass
        elif 'kr/m²' in text:
            kvm_price = int(text.replace('kr/m²', '').replace('\xa0', ''))
        elif 'rum' in text:
            rooms = float(text.replace('rum', '').replace(' ', '').replace('\xa0', '').replace(',', '.'))
        elif 'kr/mån' in text:
            rent = int(text.replace('kr/mån', '').replace(' ', '').replace('\xa0', ''))
        elif 'kr/år' in text:
            running_costs = int(text.replace('kr/år', '').replace(' ', '').replace('\xa0', ''))
        elif 'm²' in text:
            kvm = float(text.replace('m²', '').replace(' ', '').replace('\xa0', '').replace(',', '.'))
        elif 'kr' in text:
            price = int(text.replace('kr', '').replace(' ', '').replace('\xa0', ''))
        else:
            pass


    return {
        'kvm_price':kvm_price,
        'rooms':rooms,
        'rent':rent,
        'running_costs':running_costs,
        'kvm':kvm,
        'build_year':build_year,
        'price':price,
    }


if __name__ == '__main__':
    new_path = 'tmpObject.html'
    doc = open(new_path, mode='r', encoding="utf-8").read()
    print(parse(doc))

    print('done')