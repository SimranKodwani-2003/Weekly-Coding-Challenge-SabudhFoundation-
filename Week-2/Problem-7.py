m=[[1,2,3],[4,5,6],[7,8,9]]
l=len(m)
for i in range(l):
    for j in range(i+1,l):
        m[i][j], m[j][i]=m[j][i], m[i][j]
           
for row in m:
        row.reverse()

print(m)