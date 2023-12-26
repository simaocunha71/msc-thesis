
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    
    # base case:
    if n % 2 ==0 and (n%2)==0 and (n/2)-1<4:
        return True
    else:
        return False

# driver code
if __name__ == '__main__':
    test_cases = [ 1, 2 ]
    print(is_equal_to_sum_even(4))
