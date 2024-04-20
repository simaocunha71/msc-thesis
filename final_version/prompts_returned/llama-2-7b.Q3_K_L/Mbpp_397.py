"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""

def median_numbers(a):
    if len(a)==1: return 0
    else :
        i=2
        sum = 0
        while i<len(a)-1:
            sum += a[i]
            i+=1
            
        mid = (sum - int(sum/3))//3
        if mid == 0 or abs(int(sum / 3) - mid) > 0.5:
            return mid
        else : return sum // 3
        
"""
Given three sorted lists of integers, find the median of the sorted lists.
The median is defined as the middle element if the list has an even number of elements,
and as the mean of the two middle elements if it has an odd number of elements.
If the function returns None or a value different than the expected value for any of these test cases, your algorithm will not be accepted.