

def left_count_occurance(array,x):

    start = 0

    end = len(array) - 1

    left_side_counts = 0

    while start<=end:

        middle = start + (end-start)//2

        if array[middle] == x:

            left_side_counts = left_side_counts + 1

            end = middle - 1

        elif array[middle] < x:

            start = start + 1
        
        else:

            end = middle - 1

    return left_side_counts


def right_count_occurance(array,x):

    start = 0

    end = len(array) - 1

    right_side_counts = 0

    while start<=end:

        middle  = start + (end-start)//2

        if array[middle] == x:

            right_side_counts = right_side_counts + 1

            start = middle +  1

        elif array[middle] < x:

            start = start + 1
        
        else:

            end = middle - 1


    return right_side_counts


result = left_count_occurance([0,0,1,1,1,2,3],1) + right_count_occurance([0,0,1,1,1,2,3],1)

print(result)