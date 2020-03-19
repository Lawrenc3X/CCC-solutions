quarters = int(input())
m1 = int(input()) #35, +30
m2 = int(input()) #100, +60
m3 = int(input()) #10, +9
rounds = 0

while quarters:
    quarters -= 1
    rounds += 1
    if rounds % 3 == 1:
        m1 += 1
        if m1 == 35:
            m1 = 0
            quarters += 30
    elif rounds %3 == 2:
        m2 += 1
        if m2 == 100:
            m2 = 0
            quarters += 60
    else:
        m3 += 1
        if m3 == 10:
            m3 = 0
            quarters += 9

print("Martha plays %d times before going broke." % rounds)
