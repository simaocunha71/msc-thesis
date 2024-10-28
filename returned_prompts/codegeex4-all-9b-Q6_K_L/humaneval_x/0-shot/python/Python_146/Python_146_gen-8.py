def specialFilter(nums):
    def is_odd(num):
        return num % 2 != 0

    def first_last_odd(num):
        return is_odd(int(str(num)[0])) and is_odd(int(str(num)[-1]))

    return sum(1 for num in nums if num > 10 and first_last_odd(num))

print(specialFilter([15, -73, 14, -15]))  # 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # 2

The function specialFilter takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and both first and last digits of a number are odd. It uses two helper functions: is_odd() to check if a number is odd and first_last_odd() to check if the first and last digits of a number are odd. The function returns the sum of 1 for each element in the array that meets the criteria.