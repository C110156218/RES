M = int(input("請輸入階承值M"))
N = 0
NR = 1
while NR < M:
    N += 1
    NR = NR * N
print("超過M為",M,"的最小階層N值為:",N)