x = int(input("請輸入X軸座標"))
y = int(input("請輸入Y軸座標"))
if x == 0 and y == 0:
    print("此座標在原點上")
elif x >= 0 and y >= 0:
    print("此座標在第一象限上，距離原點",(x * x + y * y) ** 0.5)
elif x <= 0 and y >= 0:
    print("此座標在第二象限上，距離原點",(x * x + y * y) ** 0.5)
elif x <= 0 and y <= 0:
    print("此座標在第三象限上，距離原點",(x * x + y * y) ** 0.5)
elif x >= 0 and y <= 0:
    print("此座標在第四象限上，距離原點",(x * x + y * y) ** 0.5)