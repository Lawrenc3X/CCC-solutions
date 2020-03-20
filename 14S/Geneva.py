import sys
input = sys.stdin.readline

tests = int(input())

for i in range(tests):
    cars = int(input())
    mountain = [int(input()) for i in range(cars)]
    branch = []
    nextNum = 1

    while 1:
        popped = False

        if not(mountain) and not(branch):
            print("Y")
            break
        
        if branch:
            if branch[-1] == nextNum:
                branch.pop()
                nextNum += 1
                continue

        for i in mountain[::-1]:
            if i == nextNum:
                mountain.pop()
                popped = True
                nextNum += 1
                break
            branch.append(mountain.pop())

        if not(popped):
            print("N")
            break
