W, D = [int(i) for i in input().split()]
print("Sun Mon Tue Wed Thr Fri Sat")
for i in range((W * 2) - 1):
    print("  ", end = "")
for i in range(1, D + 1):
    if i == D: #last day
        print(i)
    elif not((W + (i - 1)) % 7):#end of line
        print(i)
        if i - 9 < 0:
            print("  ", end = "")
        else:
            print(" ", end = "")
    else: #regular case
        if (i+1) - 10 < 0:
            print("%d   " % i, end = "")
        else:
            print("%d  " % i, end = "")
