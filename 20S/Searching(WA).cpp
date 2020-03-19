// !!!!!!!!!!! Implementation of Pierce's idea!!!!!!!!!!!
//
// needle = input()
// haystack = input()
// needle_length = len(needle)
// 
// def Occurences(s):
//     array = [0] * 26
// 
//     for i in s:
//         array[ord(i) - 97] += 1
// 
//     return array
// 
// signature = Occurences(needle)
// # print(signature)
// 
// perm = 0
// previous = []
// for i in range(len(haystack) - needle_length + 1):
//     view = haystack[i: i + needle_length]
// 
//     if Occurences(view) == signature:
//         if view not in previous:
//             perm += 1
//             previous.append(view)
// 
// print(perm)

#include <stdio.h>
#include <vector>
#include <string.h>

#define MAX 200000
#define ALPHA 26

char needle[MAX], haystack[MAX];
int needleLength, haystackLength = MAX;

bool arrayEqual(int * a1, int * a2, int size)
{
    for (int i = 0; i < size; i ++)
    {
        if (a1[i] != a2[i])
        {
            return false;
        }
    }
    return true;
}

bool in (char * s, std::vector<char *> v)
{
    for (int i = 0; i < v.size(); i ++)
    {
        if (strcmp(s, v[i]) == 0)
        {
            return true;
        }
    }
    return false;
}

int * Occurences(char * s, int size, int * array)
{
    for (int i = 0; i < ALPHA; i++)
    {
        array[i] = 0;
    }

    for (int i = 0; i < size; i ++)
    {
        int ord = s[i];
        array[ord - 97] += 1;
    }

    return array;
}

int main()
{
    scanf("%s", needle);
    scanf("%s", haystack);

    for (int i = 0; i < MAX; i ++)
    {
        if (needle[i] == '\0' && needleLength == MAX)
        {
            needleLength = i;
        }

        if (haystack[i] == '\0' && haystackLength == MAX)
        {
            haystackLength = i;
        }

        if (needleLength != MAX && haystackLength != MAX)
        {
            break;
        }
    }
    
    int signature[ALPHA];
    Occurences(needle, needleLength, signature);
    
    for (int i = 0; i < ALPHA; i ++)
    {
        printf("%d\n", signature[i]);
    }
    printf("\n");

    int perm = 0;
    std::vector<char *> previous;
    for (int i = 0; haystackLength - needleLength + 1; i++)
    {
        char * rbound;
        char view[needleLength];
        
        strncpy(rbound, haystack, i + needleLength);
        strcat(view, rbound + i);

        int view_signature[ALPHA];
        Occurences(view, needleLength, view_signature);

        if (arrayEqual(view_signature, signature, needleLength) )
        {
            if (in(view, previous) )
            {
                perm += 1;
                previous.push_back(view);
            }
        }
    }

    printf("%d", perm);
}
