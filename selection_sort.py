
# selection sort algorithm

def selection_sort(array):

    size = len(array)-1

    for Index in range(size):

        small_index  = Index

        for element_index in range(Index+1, size+1):

            if array[element_index]<array[small_index]:

                small_index =  element_index

        if Index!=small_index:

            array[Index],array[small_index] = array[small_index],array[Index]
    
    return array




result = selection_sort([9,0,3,23,15,0.1,-1,100,99,19,1])

print(result)