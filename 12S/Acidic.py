import sys
input = sys.stdin.readline

sensors = int(input())
readings = [int(input()) for i in range(sensors)]
frequencies = [0 for i in range(max(readings) + 1)]

for i in readings:
    frequencies[i] += 1

frequencies = [(reading, frequency) for reading, frequency in enumerate(frequencies)]
frequencies.sort(reverse = True, key = lambda x: x[1])

tops = 1
seconds = 1

for index, i in [j for j in enumerate(frequencies)][:-1]:
    if i[1] == frequencies[index + 1][1]:
        tops += 1
    else:
        break

if tops < 2:
    for index, i in [j for j in enumerate(frequencies)][1:-1]:
        if i[1] == frequencies[index + 1][1]:
            seconds += 1
        else:
            break

first = frequencies[0][0]
second = frequencies[1][0]

if tops > 2:
    print(max([i[0] for i in frequencies[:tops] ]) - min([i[0] for i in frequencies[:tops] ]) )
elif tops == 2:
    print(abs(first - second) )
elif seconds > 1:
#     tops greater
    diff1 = abs(first - min([i[0] for i in frequencies[tops: tops + seconds] ]))
#     seconds greater
    diff2 = abs(max([i[0] for i in frequencies[tops: tops + seconds] ]) - first)

    print(max(diff1, diff2))
else:
    print(abs(first - second))
