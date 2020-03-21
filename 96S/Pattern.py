cases = int(input())

def combos(total, ones):
    if ones == 0:
        yield "0" * total
    elif ones == 1:
        for i in range(total):
            yield "0" * i + "1" + "0" * (total - (i + 1) )
    elif ones == 2:
        for i in range(total - 1):
            prependix = "0" * i + "1"
            for j in range(total - (i + 1) ):
                yield prependix + "0" * j + "1" + "0" * (total - (i + 1) - (j + 1) ) 
    else:
        for i in range(total - ones + 1):
            for combo in combos(total - (i + 1), ones - 1):
                yield "0" * i + "1" + combo

for i in range(cases):
    total, ones = [int(i) for i in input().split(" ")]

    print("The bit patterns are")
    for i in combos(total, ones):
        print(i)
