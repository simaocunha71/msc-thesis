    def will_it_fly(q,w):
        if str(q) != str(q)[::-1]:
            return False
        return sum(q) <= w
    # Test cases:
    print(will_it_fly([1, 2], 5))  # False
    print(will_it_fly([3, 2, 3], 1))  # False
    print(will_it_fly([3, 2, 3], 9))  # True
    print(will_it_fly([3], 5))  # True
    print(will_it_fly([1,2,3,4,5], 10))  # True
    print(will_it_fly([1,2,3,4,5], 5))  # False
    print(will_it_fly([1,2,3,4,5], 9))  # False
    print(will_it_fly([1], 10))  # True
    print(will_it_fly([1], 5))  # True
    print(will_it_fly([1], 4))  # False
    print(will_it_fly([], 5))  # True
    print(will_it_fly([], 0))  # True
    print(will_it_fly([], -1))  # True
    print(will_it_fly([], -5))  # True
    print(will_it_fly([], -10))  # True
    print(will_it_fly([], 10))  # True
    print(will_it_fly([], 5))  # True
    print(will_it_fly([], 4))  # True
    print(will_it_fly([], 3))  # True
    print(will_it_fly([], 2))  # True
    print(will_it_fly([], 1))  # True
    print(will_it_fly([], 0))  # True
    print(will_it_fly([], -1))  # True
    print(will_it_fly([], -2))  # True
    print(will_it_fly([], -3))  # True
    print(will_it_fly([], -4))  # True
    print(will_it_fly([], -5))  # True
    print(will_it_fly([], -6