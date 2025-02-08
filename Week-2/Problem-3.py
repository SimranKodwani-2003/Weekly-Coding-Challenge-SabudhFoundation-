def Arr_sum(N,given_sum):
    count=0
    c=[]
    for i in range(len(N)):
        sum=N[i]+N[i-1]
        if sum==given_sum:
            count+=1
            c.append(sum)
    return count
N=[1, 5, 7, -1, 5]
k=Arr_sum(N,6)
print(k)