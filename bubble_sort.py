


def bubble_sort(array):

    size=len(array)-1

    if size==-1:

        return -1

    

    for i in range(0,size-1):

        swap = False

        for j in range(0,size-i):

            if array[j]>array[j+1]:

                array[j],array[j+1]=array[j+1],array[j]

                swap=True

        if swap==False:

            return array


    return array

result=bubble_sort([])

print(result)