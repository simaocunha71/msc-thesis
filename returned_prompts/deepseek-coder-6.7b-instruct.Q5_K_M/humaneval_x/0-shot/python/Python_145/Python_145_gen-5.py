
    def sum_digits(n):
        if n < 0:
            n = -n
        return sum(map(int, str(n)))

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))


if __name__ == "__main__":
    print(order_by_points([1, 11, -1, -11, -12]))  # == [-1, -11, 1, -12, 11]
    print(order_by_points([]))  # == []


Note:

The function sum_digits is used to calculate the sum of the digits of a number.

The function order_by_points sorts the list of numbers by the sum of their digits using the sorted function with a key.

The key is a tuple where the first element is the sum of the digits and the second element is the index of the number in the original list.

The sorted function uses the first element of the tuple (the sum of the digits) to sort the numbers first and then uses the second element of the tuple (the index of the number in the original list) to resolve ties.

The sorted function returns a new sorted list and does not modify the original list.
"""

# Solution 2

def order_by_points(nums):
    return sorted(nums, key=lambda x: (sum(map(int, str(abs(x))))))

if __name__ == "__main__":
    print(order_by_points([1, 11, -1, -11, -12]))  # == [-1, -11, 1, -12, 11]
    print(order_by_points([]))  # == []

"""
This solution is similar to the previous one but uses the built-in map and sum functions to calculate the sum of the digits of a number in a more concise way.

The sorted function uses the sum of the digits as the key to sort the numbers in ascending order.

The sorted function returns a new sorted list and does not modify the original list.
"""
<jupy