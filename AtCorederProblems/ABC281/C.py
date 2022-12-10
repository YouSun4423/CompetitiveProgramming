N, T = map(int, input().split())
A = list(map(int, input().split()))

A_total = sum(A)
T_mod = T%A_total

i=0
while True:
    remand = T_mod
    remand -= A[i]
    if remand <= 0:
        print(i+1, T_mod)
        exit()
    T_mod = remand
    i += 1