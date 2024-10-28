    def will_it_fly(q,w):
        if q == q[::-1]: # check if it's balanced
            return sum(q) <= w # check if the sum of its elements is less than or equal the maximum possible weight
        else:
            return False
    print(will_it_fly([1, 2], 5)) # False 
    print(will_it_fly([3, 2, 3], 1)) # False
    print(will_it_fly([3, 2, 3], 9)) # True
    print(will_it_fly([3], 5)) # True
    # Output: 
    # False 
    # False
    # True
    # True


