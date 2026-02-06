
# def indsertion_sort(array):

#     size = len(array)-1

#     for i in range(size):

#         Index = i + 1

#         for __ in range(0, Index):


#             if array[Index] < array[Index-1]:

#                 array[Index],array[Index-1] = array[Index-1],array[Index]

#                 Index = Index - 1

#             else: 

#                 break

#     return array


# result = indsertion_sort([5,1,4])

# print(result)


def insertion_sort_while(array):

    n = len(array)

    for i in range (1,n):

        index = i

        while index > 0 and array[index] < array[index-1]:

            array[index],array[index-1] = array[index-1],array[index]

            index = index - 1

    return array

result = insertion_sort_while([9,7,0,12,34,8,6,5])

print(result)
