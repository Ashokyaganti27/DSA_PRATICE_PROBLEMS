


# def checksorted(li):

#     if (len(li)==1 or len(li)==0):

#         return True 
    
#     ans = checksorted(li[1:])

#     if li[0] < li[1]:

#         return ans
    
#     return False 

# print(checksorted([2,8,9,13,14]))


def checsorted(li):

    if (len(li)==1 or len(li)==0):

        return True
    
    if li[0] > li[1]:

        return False
    
    return checsorted([li[1:]])


print(checsorted([2,3,4,5,6,7,8]))
