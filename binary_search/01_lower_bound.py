

def lowerBound(nums, x):

        start = 0

        end = len(nums) -1 

        Index = len(nums)


        while end>=start:

            middle = start+(end-start)//2


            if nums[middle] == x:

                Index = middle

                end = middle - 1

            elif nums[middle] < x:
                
                start = middle + 1

            elif nums[middle] > x:

                Index = middle

                end = middle - 1
    
        return Index

result = lowerBound([3,5,8,15,19],56)
                    

print(result)

       


