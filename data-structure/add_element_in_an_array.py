#!/usr/bin/env python3

def add_ele(arr, pos, val):
    result = [0] * (len(arr)+1)
    # result = arr
    
    for x in range(len(arr)):
        if x == pos:
            result[x] = val
            break
        else:
            result[x] = arr[x]

    
    for x in range(len(result)):
        print(x, pos)
        if x > pos:
            result[x] = arr[x-1]
        

    print(result)
    return arr


arr = [1,5,6,8,2,12321,213,23,233,90]
add_ele(arr, 6, 7)