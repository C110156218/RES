n = int(input())
if n < 121:
    print("Summer Months:",n * 2.10)
    print("Non Summer Months:",n * 2.10)
elif n < 331:
    print("Summer Months:",((n -120) * 3.02) + (120 * 2.10))
    print("Non Summer Months:",((n -120) * 2.68) + (120 * 2.10))
elif n < 501:
    print("Summer Months:",((n -330) * 4.39) + (210 * 3.02)+ (120 * 2.10))
    print("Non Summer Months:",((n -330) * 3.61) + (210 * 2.68)+ (120 * 2.10))
elif n < 701:
    print("Summer Months:",((n -500) * 4.97) +(170 * 4.39) + (210 * 3.02)+ (120 * 2.10))
    print("Non Summer Months:",((n -500) * 4.01) +(170 * 3.61) + (210 * 2.68)+ (120 * 2.10))
else:
    print("Summer Months:",((n -700) * 5.63) +(200 * 4.97) +(170 * 4.39) + (210 * 3.02)+ (120 * 2.10))
    print("Non Summer Months:",((n -700) * 4.50) +(200 * 4.01) +(170 * 3.61) + (210 * 2.68)+ (120 * 2.10))