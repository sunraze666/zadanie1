delitel = 0

for i in range(1, 2000):
    if 1260 % i == 0 and 3400 % i == 0:
        delitel = i
print(delitel)
