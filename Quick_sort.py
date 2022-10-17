"""Implement quick sort in Python.
Input a list.
Output a sorted list."""



def quicksort(array):
    """ My 1st version of the quick search from scratch """
    size = len(array)
    if size <= 1:
        return array            
    else:
        pivot = array[size-1]
        pivot_ind = size-1
        i = 0
        while i < pivot_ind:
            if array[i] > pivot:
                array[pivot_ind] = array[i] 
                array[i] = array[pivot_ind-1]
                array[pivot_ind-1] = pivot
                pivot_ind = pivot_ind-1
            else:
                i += 1
        
        left_list = quicksort(array[:pivot_ind])
        right_list = quicksort(array[pivot_ind+1:])
        
        left_list.append(pivot)
            
        return left_list + right_list

#Love this solution from #stackoverflow, so buitiful, less extra variables
def quicksort2(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort2(less) + equal + quicksort2(greater) 
    else:
        return array


test = [21, 4, 1, 3, 14, 20, 25, 6, 21, 14]
test2 = [20,3]
#print(quicksort1(test))
print(quicksort(test))