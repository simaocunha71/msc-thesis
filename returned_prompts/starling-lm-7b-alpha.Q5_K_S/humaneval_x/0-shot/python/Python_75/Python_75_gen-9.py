    def is_prime(n):
        """A function that returns true if the given number is prime and false otherwise"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_multiply_prime(a):
        """Write a function that returns true if the given number is the multiplication of 3 prime numbers
        and false otherwise."""
        if a < 10:
            return False

        nums = [2, 3, 5]
        if a == 4:
            return False
        else:
            for i in range(4, a):
                if is_prime(i):
                    nums.append(i)
        if len(nums) != 3:
            return False
        else:
            if nums[0] * nums[1] * nums[2] == a:
                return True
            else:
                return False


# print(is_multiply_prime(30))
# print(is_multiply_prime(49))
# print(is_multiply_prime(71))
# print(is_multiply_prime(73))
# print(is_multiply_prime(75))
# print(is_multiply_prime(78))
# print(is_multiply_prime(91))

# def is_multiply_prime(a):
#     """Write a function that returns true if the given number is the multiplication of 3 prime numbers
#     and false otherwise.
#     Knowing that (a) is less then 100. 
#     Example:
#     is_multiply_prime(30) == True
#     30 = 2 * 3 * 5
#     """

#     def is_prime(n):
#         """A function that returns true if the given number is prime and false otherwise"""
#         if n < 2:
#             return False
#         for i in range(2, int(n ** 0.