import re
import pprint
input_file = open('input.txt')
output_file = open('output.txt', 'w')

data_list = ['']
i = 0
for line_n, line in enumerate(input_file):
    items = line.split('\t')
    print items
    text = ''
    sentence = items[12].strip()
    if sentence[0] == "1" or sentence[0] == "2":
        i += 1
        data_list.insert(i, sentence + "|")
        for j in items[15:]:
            data_list[i] += j + ' '
    else:
        data_list[i - 1] += sentence + "|"
        for j in items[15:]:
            data_list[i-1] += j + ' '
    data_list[i].strip()
#pprint.pprint(pom)

for item in data_list:
    output_file.write(item.strip()+'')

#output_file.write(pom)
