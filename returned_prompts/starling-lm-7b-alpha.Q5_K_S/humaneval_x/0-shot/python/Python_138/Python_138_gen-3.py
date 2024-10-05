    # import itertools
    # from itertools import product, combinations
    # from functools import reduce
    # from operator import add
    # def is_equal_to_sum_even(n):
    #     """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    #     if not n % 2 == 0 or n < 8:
    #         return False
    #     for combination in itertools.combinations(range(1, n+1), 4):
    #         if sum(combination) == n and all(i % 2 == 0 for i in combination):
    #             return True
    #     return False
    import itertools
    from itertools import product, combinations
    from functools import reduce
    from operator import add
    def is_equal_to_sum_even(n):
        """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
        if not n % 2 == 0 or n < 8:
            return False
        for combination in itertools.combinations(range(1, n+1), 4):
            if sum(combination) == n and all(i % 2 == 0 for i in combination):
                return True
        return False
    return is_equal_to_sum_even
































































































































































































