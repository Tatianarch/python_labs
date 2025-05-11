print("input a:")
a = int(input())
print("input b:")
b = int(input())
print("input c:")
c = int(input())

min, max = float("inf"), float("-inf")

if a < min:
    min = a
if b < min:
    min = b
if c < min:
    min = c

if a > max:
    max = a
if b > max:
    max = b
if c > max:
    max = c

print("Min:", min)
print("Max:", max)