
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
    
    odd_lst = []  # A list of numbers that are 'odd' (not include 0)
    neg_lst = []  # List of negative numbers
    nonint_lst = []  # Numbers that aren't ints
    
    for elm in lst:
        if elm != 0 and not isinstance(elm, float):
            odd_lst.append(elm)
        
    if not odd_lst or (len(odd_lst) == len(lst)):
        return double_the_difference(odd_lst)
    
    for elm in odd_lst:
        nonint_lst.append(abs(int(elm)-1))
        
    if not neg_lst or (len(neg_lst) == len(nonint_lst)):
        return double_the_difference(neg_lst)
    
    for elm in neg_lst:
        nonint_lst.append(-abs(int(elm)-1))
        
    if not zero_in_list(nonint_lst):
        return sum([int(n) ** 2 for n in nonint_lst]) + double_the_difference(odd_lst)
    
    else:
        print("Error - the input list was not empty")
        
def find_sum([9,8,7,6,5,4], 0):
    return sum([int(num) ** 2 for num in [9,8,7,