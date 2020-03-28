#!/usr/bin/env python3

#Rotate Array
    # Input: [1,2,3,4,5,6,7] and k = 3
    # Output: [5,6,7,1,2,3,4]
    # Explanation:
    # rotate 1 steps to the right: [7,1,2,3,4,5,6]
    # rotate 2 steps to the right: [6,7,1,2,3,4,5]
    # rotate 3 steps to the right: [5,6,7,1,2,3,4]

def rotate(arr, k):
    step = 0
    store_step = 0
    if k>0:
        store_step = -k
        step = -k

    new_arr = []
    for i in range(k):
        new_arr.append(arr[step])
        step += 1
        
    for a in range(len(arr)+store_step):
        new_arr.append(arr[a])

    print(new_arr)
         

arr = [1,2,3,4,5,6,7]
k = 3
rotate(arr, k)