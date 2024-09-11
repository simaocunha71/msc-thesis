def move_num(s):
    return "".join(filter(lambda x: not x.isdigit(), s)) + "".join(filter(lambda x: x.isdigit(), s))

# Alternate solution using regex
import re
def move_num(s):
    return re.sub(r'\d+', '', s) + re.sub(r'\D+', '', s)

# Testing
print(move_num('I1love143you55three3000thousand'))  # 'Iloveyouthreethousand1143553000'
print(move_num('Hello3World34'))  # 'HelloWorld343'





















"""
Correct Solution:
The above problem can be broken down into two parts. The first part is to remove all the digits from the given string and the second part is to concatenate all the remaining digits at the end of the string. To remove all the digits from the string, we can use the filter function along with the isdigit() function. The filter function returns a new list with all the elements for which the given function returns true. In our case, the isdigit() function returns true for all the digits and false for all the non-digits. Hence, by applying the filter function, we can remove all the digits from the given string.
After removing all the digits, we can concatenate all the remaining digits at the end of the string using the join function. The join function concatenates all the elements of the given list to form a single string. In our case, we can pass all the remaining digits as a list to the join function to form a single string.

Time Complexity: O(n), where n is the length of the given string.

Space Complexity: O(n), where n is the length of the given string.

"""

"""
The above solution can be optimized by using the re.sub function from the re module. The re.sub function is a built-in function in Python that replaces the occurrence of the pattern with the replacement string. In our case, we can use the re.sub function to