n1 = list(map(int,input().split(',')))
n2 = list(n1)
n1.sort()
n2.sort()
n2.reverse()
n1n = ""
n2n = ""
for i in n1:
    n1n += str(n1[i])
for i in n2:
    n2n += str(i)
print(int(n2n) - int(n1n))