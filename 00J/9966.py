def recognize(string):
    pairs = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
    if not(string[0] in pairs):
        return False
    elif not(string[len(string) - 1] == pairs[string[0]]):
        return False
    elif not(len(string) < 3):
        return recognize(string[1: len(string) - 1])
    else:
        return True

start = int(input())
end = int(input())
solutions = 0
for i in [str(i) for i in range(start, end + 1)]:
    if recognize(i):
        solutions += 1
print(solutions)
