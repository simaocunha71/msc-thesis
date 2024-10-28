    def will_it_fly(q, w):
        return is_palindrome(q) and sum(q) <= w

    def is_palindrome(lst):
        return str(lst) == str(lst)[::-1]

    # test the function
    print(will_it_fly([1, 2], 5))  # False
    print(will_it_fly([3, 2, 3], 1))  # False
    print(will_it_fly([3, 2, 3], 9))  # True
    print(will_it_fly([3], 5))  # True


