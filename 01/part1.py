filename = 'input.txt'

with open(filename) as file:
    lst = list(map(int, (line for line in file)))

count = 0
prev = lst[0]
for x in lst[1:]:
    if x > prev:
        count += 1
    prev = x

print(count)
