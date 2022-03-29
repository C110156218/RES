n = int(input("請輸入一個介於11和100之間的數字"))
if n >= 11 & n <= 100:
    if n % 2 == 0 and n % 11 == 0 and n % 5 != 0 and n % 7 != 0:
        print("Yes")
    else:
        print("No")
else:
    print("輸入數字錯誤")