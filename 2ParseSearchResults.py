
new_path = 'C:/git/bostad/analys/HemnetSearchResults2.html'
new_days = open(new_path, mode='r', encoding='utf-8')

linesWithLink = []
soldObjects = ''
with open(new_path, 'r') as fin:
    for line in fin:
        if line.__contains__('data-target-blank="true" href="https://www.hemnet.se/salda/'):
            startIndex = line.find("href=\"") + len('href=\"')
            endIndex = len(line)-3
            soldObjects = soldObjects + '\n' + line[startIndex:endIndex]

print(soldObjects)

new_path = 'C:/git/bostad/analys/soldObjectsUrls.csv'
new_days = open(new_path, mode='w', encoding='utf-8')
new_days.write(soldObjects)
print("done")

