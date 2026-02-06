

def upperbound(array,x):

    n = len(array) - 1

    start = 0

    end = n

    Index = n

    while end >= start:

        middle = start + (end-start)//2


        if array[middle] >  x:

            end = middle - 1

            Index =  middle

        else:

            start = middle + 1
    
    return Index

result = upperbound([3,5,8,9,15,19],19)

print(result)

