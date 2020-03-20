x = int(input())
m = int(input())

def coprime(a, b):
    for i in range(2, a//2):
        if b % i == 0 and a % i == 0:
            return True
    return False

if coprime(x, m):
    print("No such integer exists.")
else:
    count = 2
    while True:
        if (x * count) % m == 1:
            print(count)
            break
        count += 1
