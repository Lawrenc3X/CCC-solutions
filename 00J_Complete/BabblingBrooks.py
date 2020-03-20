iStreams = int(input())
streams = [int(input()) for i in range(iStreams)]

while 1:
    action = int(input())
    if action == 99: #split
        streamNum = int(input())
        toLeft = int(input())
        originalVal = streams[streamNum - 1]
        streams[streamNum - 1] = originalVal * (toLeft/100)
        streams.insert(streamNum, originalVal * (1 - (toLeft/100)))
    if action == 88: #join
        lStream = int(input())
        streams[lStream - 1] = streams[lStream - 1] + streams[lStream]
        streams.remove(streams[lStream])
    if action == 77: #end
        break

for i in streams[0:len(streams) - 1]:
    print("%d " % i, end = "")
print(int(streams[len(streams) - 1]))
