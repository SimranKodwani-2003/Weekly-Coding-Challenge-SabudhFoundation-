def app(l):
    n=[]
    p=[]
    for i in range(len(l)):
        if l[i]<0:
            n.append(l[i])
        else:
            p.append(l[i])
    return n+p

print(app([12, 11, -13, -5, 6, -7, 5, -3, -8]))