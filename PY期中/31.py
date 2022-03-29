AL = list(map(int,input().split(' ')))
A1 = [range(AL[0]) for _ in range(AL[1])]
A2 = [range(AL[0]) for _ in range(AL[1])]
for i in range(AL[0]):
    A1[i] = list(map(int,input().split(' ')))
for i in range(AL [0]):
    A2[i] = list(map(int,input().split(' ')))
for i in range(AL[0]):
    for j in range(AL[1]):
        A1[i][j]  = A1[i][j] * A2[i][j]
for i in range(AL[0]):
    for j in range(AL[1]):
       print(A1[i][j],end=" ")
    print()