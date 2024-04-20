"""
Write a function to compute the n-th power of each number in a list.
assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def nth_nums(nums,n):
    output = [None for _ in range(len(nums))] #create a new list as the return value
    nums.sort() #sorting is needed to make it efficient
    i=0
    j=1
    for item in nums:
        while i<j and item==item[i]: #to check each element until there is no repetition of an element
            output[-i]=output[-i]+item #add the element and move on to next element
            j+=1
        i+=1
    return output
        
