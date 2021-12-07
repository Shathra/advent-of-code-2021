from collections import deque

filename = 'input.txt'

with open(filename) as file:
    lst = list(map(int, (line for line in file)))

count = 0
prev = deque(lst[:3])
prev_sum = sum(prev)
for x in lst[3:]:
    y = prev.popleft()
    next_sum = prev_sum - y + x
    prev.append(x)
    if next_sum > prev_sum:
        count += 1
    prev_sum = next_sum

print(count)
