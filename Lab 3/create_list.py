from create_list import create_list

lst = create_list()
print("Список:", lst)

output = []

for i in range(1, len(lst)):
    prev, curr = lst[i - 1], lst[i]
    if curr > prev:
        output.append(curr)

print("Результат:", output)
