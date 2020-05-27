word = input()
res = ""
size = len(word)

for i in range(0, size):
    res += word[size-1-i]

print(res)
