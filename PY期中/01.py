n = str(input("請輸入一個正整數"))
if int(n) <= 1:
    index = []
    for i in n:
        index.append(int(i))
    index.sort()
    index.reverse()
    j = 0
    for i in range(len(n)):
        print(index[i],end="")
else:
    print("輸入錯誤")