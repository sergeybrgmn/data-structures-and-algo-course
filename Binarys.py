"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

from bisect import bisect_left

#My First version from scratch
def binary_search(input_array, value):
    """Bin search implementation"""
    
    arr_len = len(input_array)
    i = arr_len // 2
    step = 2

    while (i < arr_len-1) and (i > 0):
        left = input_array[i]
        right = input_array[i+1]
        if value < left:
            print("i:", i)
            i = i - max(arr_len // (2 ** step),2)
            step += 1
        elif value > right:
            print("i:", i)
            i = i + max(arr_len // (2 ** step),1)
            step += 1
        elif value == left:
            return i
        elif value == right:
            return i+1
        else:
            return -1
    if input_array[0] == value:
        return 0
    else:
        return -1

# Bin search from stack-over-flow
#Much more clear solution
def bin_search_sof1(alist, item):
    """Bin search """
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        pos = 0
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            pos = midpoint
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return (pos, found)

# Bin search using bisect
# Super short version
def bin_search_bisect(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    print("i:", i)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

#My second attempt to make the binary search with the course task constraints
def my_bin_2nd(input_array, value):
    left = 0
    right = len(input_array)-1
    found = False
    pos = 0

    while left<=right and not found:
        midpoint = (left+right) // 2
        if input_array[midpoint] == value:
            pos = midpoint
            found = True
        else:
            if value < input_array[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1
    if found:
        return pos
    else:
        return -1


test_list = [1,3,9,11,15,19,29,35,42,45,51,68,79,82,83,86,90,91,95,97]
print(len(test_list))
test_val1 = 45
test_val2 = 100
print(my_bin_2nd(test_list, test_val1))
print(my_bin_2nd(test_list, test_val2))
