import os
import ObjectParser as op

for filename in os.listdir('objects'):
    values = op.parse(open('objects/' + filename, mode='r', encoding='utf-8').read())
    print(values)

print("done")
