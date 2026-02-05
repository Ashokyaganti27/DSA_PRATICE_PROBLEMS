


def linearsearch(arr,target):

    size=len(arr)

    for index in range(size):
        
        if arr[index]==target:

            return index
        
    return -1
    
my_list=[3,7,10,4,0,67]

result=linearsearch(my_list,0)

print(result)