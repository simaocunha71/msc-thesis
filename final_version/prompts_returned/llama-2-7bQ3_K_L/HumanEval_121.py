
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    odd_sum = 0
    for i in lst: #loop over the list and check if we have an even position?
        if(i % 2 != 0): #if it is odd
            odd_sum += i
    return odd_sum