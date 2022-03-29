A = input("甲方數字:")
B = input("乙方數字:")
AR = []
BR = []
WL = ""
for i in A:
    AR.append(i)
for i in B:
    BR.append(i)
for i in range(len(AR)):
    if AR[i] == BR[i]:
        WL += "和"
    elif AR[i] == "1" and BR[i] == "5":
        WL += "贏"
    elif AR[i] == "2" and BR[i] == "1":
        WL += "贏"
    elif AR[i] == "3" and BR[i] == "2":
        WL += "贏"
    elif AR[i] == "4" and BR[i] == "3":
        WL += "贏"
    elif AR[i] == "5" and BR[i] == "4":
        WL += "贏"
    elif AR[i] == "5" and BR[i] == "1":
        WL += "輸"
    elif AR[i] == "1" and BR[i] == "2":
        WL += "輸"
    elif AR[i] == "2" and BR[i] == "3":
        WL += "輸"
    elif AR[i] == "3" and BR[i] == "4":
        WL += "輸"
    elif AR[i] == "4" and BR[i] == "5":
        WL += "輸"
print(WL)