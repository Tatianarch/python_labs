from create_list import create_list

data = create_list()
print(data)

res = [curr for i, curr in enumerate(data[1:], start=1) if curr > data[i - 1]]

print(res)
