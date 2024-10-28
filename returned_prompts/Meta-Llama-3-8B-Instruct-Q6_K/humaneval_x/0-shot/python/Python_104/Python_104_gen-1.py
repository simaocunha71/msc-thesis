def unique_digits(x):
    return sorted([i for i in x if not any(int(digit) % 2 == 0 for digit in str(i))])  # using list comprehension and generator expression to filter the numbers and sort them
# or using a for loop
# unique_digits = []
# for i in x:
#     if not any(int(digit) % 2 == 0 for digit in str(i)):
#         unique_digits.append(i)
# return sorted(unique_digits)
# or using a lambda function
# return sorted(list(filter(lambda i: not any(int(digit) % 2 == 0 for digit in str(i)), x)))
# or using a set and then converting it to list and sorting it
# return sorted(list(set(i for i in x if not any(int(digit) % 2 == 0 for digit in str(i)))))
# all of these will work and return the same result
# but the first one is the most efficient and clear one. 
# it uses list comprehension and generator expression which are more efficient and readable than for loop and filter function. 
# and it directly returns the result without creating an extra list. 
# and it is also more flexible and can be easily extended to more complex conditions. 
# and it is also more readable and understandable for others. 
# and it is also more maintainable and can be easily updated to new conditions.  # using list comprehension and generator expression to filter the numbers and sort them
# or using a for loop
# unique_digits = []
# for i in x:
#     if not any(int(digit) % 2 == 0 for digit in str(i)):
#         unique_digits.append(i)
# return sorted(unique_digits)
# or using a lambda function
# return sorted(list(filter(lambda i: not any(int(digit) % 2 == 0 for digit in str(i)), x)))
# or using a set and then converting it to list and sorting it
# return sorted(list(set(i for i in x if not any(int(digit) % 2 == 0 for digit in str(i)))))
# all of these will work and return the same result
# but the first one is the most efficient and clear one. 
# it uses list comprehension and generator expression which are more efficient and readable than for loop and filter function. 
# and it directly returns the result without creating an extra list. 
# and it is also more flexible and can be easily extended