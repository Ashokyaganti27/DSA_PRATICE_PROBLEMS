


def floor_ceil(array,x):
    
    start = 0
    end = len(array)-1

    floor = -1

    ceil = -1

    while start<=end:

        middle = start + (end-start)//2

        if array[middle] == x:

            floor = middle

            ceil = middle

            return [array[floor],array[ceil]]
        
        elif array[middle]<x:

            floor = middle

            start = middle + 1
        
        elif array[middle]>x:

            ceil = middle

            end = middle - 1

    floor = array[floor] if floor!=-1 else -1

    ceil = array[ceil] if ceil!=-1 else -1

    return [floor, ceil]


result = floor_ceil([3,5,7,9,10,12,15],20)

print(result)