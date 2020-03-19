# !!!!!!!!!!! Implementation of Pierce's idea!!!!!!!!!!!

needle = input()
haystack = input()
needle_length = len(needle)

def Occurences(s):
    array = [0] * 26

    for i in s:
        array[ord(i) - 97] += 1

    return array

signature = Occurences(needle)
#  print(signature)

perm = 0
previous = []
# for i in range(len(haystack) - needle_length + 1): # implement rolling table
#     view = haystack[i: i + needle_length]
# 
#     if Occurences(view) == signature:
#         if view not in previous:
#             perm += 1
#                previous.append(view)

print(perm)
