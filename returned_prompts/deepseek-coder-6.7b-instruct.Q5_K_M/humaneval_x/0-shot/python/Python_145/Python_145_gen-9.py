
    def sum_of_digits(num):
        return sum(map(int, str(abs(num))))

    return sorted(nums, key=lambda num: (sum_of_digits(num), nums.index(num)))

print(order_by_points([1, 11, -1, -11, -12])) #== [-1, -11, 1, -12, 11]
print(order_by_points([])) #== []

# 1. sum_of_digits is a helper function that returns the sum of the digits of a number.
# 2. The sorted function sorts the nums list according to two conditions:
#       a) The sum of the digits of each number, b) the index of each number in the original list.
# 3. The lambda function is used to create a function on the fly that returns a tuple of the sum of the digits and the index of each number.
# 4. The sorted function returns a new sorted list of the original nums list.
# 5. The lambda function is used to create a function on the fly that returns a tuple of the sum of the digits and the index of each number.
# 6. The sorted function returns a new sorted list of the original nums list.
# 7. The lambda function is used to create a function on the fly that returns a tuple of the sum of the digits and the index of each number.
# 8. The sorted function returns a new sorted list of the original nums list.
# 9. The lambda function is used to create a function on the fly that returns a tuple of the sum of the digits and the index of each number.
# 10. The sorted function returns a new sorted list of the original nums list.
# 11. The lambda function is used to create a function on the fly that returns a tuple of the sum of the digits and the index of each number.
# 12. The sorted function returns a new sorted list of the original nums list.
# 13. The lambda function is used to create a function on the fly that returns a tuple of the sum of the digits and the index of each number