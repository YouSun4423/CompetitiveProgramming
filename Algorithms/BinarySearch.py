def binary_search(N, A, k):
    ans = -1
    l = 0
    r = N - 1
    while r-l+1>=1:
        m = (r+l) // 2
        if A[m] == k:
            ans = m
            print(ans)
            return m
        if A[m] < k:
            l = m + 1
        if A[m] > k:
            ans = m
            r = m - 1
    print(ans)
    return -1


N, k = map(int, input().split())
#配列A
a=list(map(int,input().split()))

#関数を実行
binary_search(N,a,k)