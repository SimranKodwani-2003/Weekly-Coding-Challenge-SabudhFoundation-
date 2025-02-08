def arr_diff(N,m):
    if len(N)==0 or m==0:
        return 0
    if len(N)<m:
        return -1
    N.sort()
    min_diff=float("inf")
    for i in range(len(N)-m+1):
        diff=N[i+m-1]-N[i]
        min_diff=min(min_diff,diff)
    return min_diff
    
N=[3, 4, 1, 9, 56, 7, 9, 12]
print(arr_diff(N,5))