line = input()
freq = {}

for ch in line.replace(" ", ""):
    if ch not in freq:
        freq[ch] = line.count(ch)

for i in range(3):
    top_ch = max(freq, key=freq.get)
    print(top_ch, freq[top_ch])
    freq.pop(top_ch)