


def roted_soted_array(array,target):

    start = 0

    end = len(array)-1

    while start<=end:

        middle = start  + (end-start)//2

        if array[middle] == target:

            return middle
        
        if array[start] <= array[middle]:

            if array[start] <= target < array[middle]:

                end  = middle - 1

            else:

                start = middle + 1
        else:

            if array[middle] < target <= array[end]:

                start = middle + 1

            else:

                end = middle - 1


    return -1


result = roted_soted_array([14,17,18,19,20,34,3,8,9,10,12],14)

print(result)