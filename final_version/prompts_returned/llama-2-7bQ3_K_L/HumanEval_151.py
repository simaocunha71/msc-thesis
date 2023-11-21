
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    if not lst:
        return 0
    
    sum = []

    for num in lst:
        if isinstance(num, int) and ((num%2 == 1 or is_odd(num)) and (abs(num) > -1)):
            sum.append((num * num))
            
        elif isinstance(num, list):
            sum += double_the_difference(num)
        
    return sum[0]
