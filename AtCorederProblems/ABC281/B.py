import re

S = input()
number = re.sub(r"\D", "", S)

if not len(S) == 8:
    print('No')
    exit()

for i, s in enumerate(S):
    if i == 0 and i == 7:
        if not s.isupper():
            print('No')
            exit()

if not len(number) == 6:
    print('No')
    exit()

if not (100000 <= int(number) <= 999999):
    print('No')
    exit()

print('Yes')