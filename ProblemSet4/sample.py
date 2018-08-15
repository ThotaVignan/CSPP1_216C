d = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
sequence = input()
freq = {}
for x in sequence:
    freq[x] = freq.get(x,0) + 1
print(freq)
print(d)
for letter in sequence:
	print(d[letter])
	if d[letter] != sequence[letter]:
		print("Not equal")
