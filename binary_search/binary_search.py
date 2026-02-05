

# def binary_search(arr,target):

#     if len(arr)==0:

#         return "array has zero elements"
     
#     start=0

#     end=len(arr)-1


#     while end>=start:
#         middle= start+(end-start)//2

#         if arr[middle]==target:

#             return middle
        
#         elif arr[middle]<target:

#             start=middle+1


#         else:

#             end=middle-1
    
#     return -1

# my_list=[1]

# target=0

# result=binary_search(my_list,target)
# print(result)

def first_occurance_binary_search(arr,target):

    if len(arr)==0:

        return -1
     
    start=0
    
    first_occurance=-1

    end=len(arr)-1


    while end>=start:
        middle= start+(end-start)//2
        
        if arr[middle]==target:

            first_occurance=middle

            end=middle-1
        
        elif arr[middle]<target:

            start=middle+1


        else:

            end=middle-1
    
    return first_occurance


# arr = [1,1,1,1,1]
# target = 0


# result=first_occurance_binary_search(arr,target)
# print(result)

def last_occurance_binary_search(arr,target):

    if len(arr)==0:

        return -1
     
    start=0
    
    last_occurance=-1

    end=len(arr)-1


    while end>=start:

        middle= start+(end-start)//2
        
        if arr[middle]==target:

            last_occurance=middle

            start=middle+1
        
        elif arr[middle]<target:

            start=middle+1


        else:

            end=middle-1
    
    return last_occurance


arr = [1,2,3,4,6,6,6,6,6,67]
target = 6


result=(first_occurance_binary_search(arr,target),last_occurance_binary_search(arr,target))
print(result)
