def sum_of_digits(nums):
    s = 0
    for n in nums:
        while n > 0:
            s += n % 10
            n = n // 10
    return s

def test_sum_of_digits():
    assert sum_of_digits([10,2,56])==14

test_sum_of_digits()


# Another approach using map and reduce
def sum_of_digits_mapreduce(nums):
    return sum(map(lambda n: sum(map(int, str(n))), nums))

def test_sum_of_digits_mapreduce():
    assert sum_of_digits_mapreduce([10,2,56])==14

test_sum_of_digits_mapreduce()

"""
The function sum_of_digits(nums) computes the sum of digits of each number of a given list. It first initializes a variable s to 0 to store the sum of digits. Then, for each number n in the list, it enters a while loop that continues until n becomes 0. In each iteration, it adds the last digit of n (the remainder of n divided by 10) to s. Then, it updates n by integer division by 10. After the while loop, it returns the sum of digits s.

The function test_sum_of_digits() is a unit test that checks if sum_of_digits([10,2,56]) returns 14, which is the expected result.

The function sum_of_digits_mapreduce(nums) is an alternative implementation of sum_of_digits() using map and reduce. It first uses map to convert each number in nums to a list of its digits, then uses map again to convert each digit to an integer. Finally, it uses sum to add all the digits together.

The function test_sum_of_digits_mapreduce() is a unit test that checks if sum_of_digits_mapreduce([10,2,56]) returns 14, which is the expected result.
"""


# Python3
"""
