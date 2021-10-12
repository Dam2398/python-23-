import re

file = open("regex_sum_912015.txt", 'r')

y = re.findall('[0-9]+', file.read())

num = list(map(int, y))

sum = 0
for i in num:
    sum = sum+i

print(sum)
