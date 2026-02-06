

'''Problem Statement: You are given a sorted array arr of distinct values and a target value x. "
You need to search for the index of the target value in the array.'''



'''
Example 1:
Input Format: arr[] = {1,2,4,7}, x = 6
Result: 3
Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

Example 2:
Input Format: arr[] = {1,2,4,7}, x = 2
Result: 1
Explanation: 2 is present in the array and so we will return its index i.e. 1.

'''

def search_insert_position(array,x):

    size = len(array) - 1

    start = 0
    end = size

    Index = len(array)

    while end >= start:

        middle = start + (end-start)//2

        if array[middle]==x:

            Index = middle

            return Index
        
        elif array[middle] > x:

            Index = middle

            end = middle - 1
        else:

            start = middle + 1

    return Index

result = search_insert_position([1,2,3,4],5)

print(result)
