"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""

def find_max_product(arr):
    ''' 
       FIND THE MAXIMUM PRODUCT OF INTEGERS FROM AN INPUT ARRAY
    '''    
    max_prod = []
    for i in arr:
        if i not in max_prod:
            max_prod.append((i,arr[i])) # [10],[10]
        
    for j in range(len(max_prod)):
        product = 1
        for k in range(j+1,len(max_prod)):
            if not (k==j or k==0):
                prod = max_prod[j][1]*max_prod[k][1]   # 1*2=2, 1*3=3...
                product *= prod
            else:   
                continue    
        if product > max_prod[j]:
            max_prod[j],max_prod[j+1]=max(max_prod[j+1],(max_prod[j+1],max_product),(j,product))   # j, (4) -> (3,6),(2,5)->..., (0,7)
    return max_prod
                               
    
# if __name__=="__main__": 
#     find_highest_product = find_max_product([-1,-2,-3])
        