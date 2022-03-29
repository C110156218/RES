from unittest import case


n = list(map(int,input().split(',')))
if n[0] == 186:
    if n[1]*0.09 <= 186:
        print("通話費為:",round(n[1]*0.09))
    elif n[1]*0.09 <= 186 * 2:
        print("通話費為:",round(n[1]*0.09*0.9))
    else:
        print("通話費為:",round(n[1]*0.09*0.8))
elif n[0] == 386:
    if n[1]*0.09 <= 386:
        print("通話費為:",round(n[1]*0.08))
    elif n[1]*0.09 <= 386 * 2:
        print("通話費為:",round(n[1]*0.08*0.8))
    else:
        print("通話費為:",round(n[1]*0.08*0.7))
elif n[0] == 586:
    if n[1]*0.09 <= 586:
        print("通話費為:",round(n[1]*0.07))
    elif n[1]*0.09 <= 586 * 2:
        print("通話費為:",round(n[1]*0.07*0.7))
    else:
        print("通話費為:",round(n[1]*0.07*0.6))
elif n[0] == 986:
    if n[1]*0.09 <= 586:
        print("通話費為:",round(n[1]*0.06))
    elif n[1]*0.09 <= 586 * 2:
        print("通話費為:",round(n[1]*0.06*0.6))
    else:
        print("通話費為:",round(n[1]*0.06*0.6))
else:
    print("輸入錯誤")