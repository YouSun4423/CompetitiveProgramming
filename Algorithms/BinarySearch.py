def binary_search(N, A, x):
    l = 0
    r = N - 1
    while r-l+1>=1:
        m = (r+l) // 2
        if A[m] == x:
            print(m)
            return m
        elif A[m] < x:
            l = m + 1
        elif A[m] > x:
            r = m - 1
    return -1

#配列の長さ
n=int(input())
#配列A
a=list(map(int,input().split()))
#見つけたい値
x=int(input())

#関数を実行
binary_search(n,a,x)