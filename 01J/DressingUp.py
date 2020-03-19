height = int(input())
for i in range(-(2 * height - 2), 2 * height - 1, 4):
    space = abs(i)
    stars = ((2 * height - space)//2)
    line  = "*" * stars + " " * space + "*" * stars
    print(line)
