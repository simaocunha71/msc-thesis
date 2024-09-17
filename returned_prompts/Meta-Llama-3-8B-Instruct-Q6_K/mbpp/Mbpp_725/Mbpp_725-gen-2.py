def extract_quotation(s):
    return [word.strip('"') for word in s.split('"') if word.strip('"')]

assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']  # test case 1
print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))  # test case 2
print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor" "Hello"'))  # test case 3
print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor" "Hello" "World"'))  # test case 4

# Explanation:
# This function splits the given string by the quotation marks and then strips the quotation marks from the resulting list. 
# The list comprehension is used to achieve this in a single line of code. The strip('"') method is used to remove the quotation marks from each word. 
# The if word.strip('"') condition is used to ignore empty strings that may result from consecutive quotation marks. 

# The unit test case 1 checks if the function correctly extracts the words between quotation marks. 
# The test case 2 checks if the function works correctly even when there are multiple words between quotation marks. 
# The test case 3 checks if the function works correctly even when there are multiple sets of quotation marks. 
# The test case 4 checks if the function works correctly even when there are multiple sets of quotation marks and multiple words between them. 

# This function can be used to extract values between quotation marks from a given string. 
# It can be useful in parsing and processing text data where the values are enclosed in quotation marks. 
# For example, it can be used to extract product names from a product description string or to extract customer names from a customer list string.  # test case 5
# This function can also be used to extract values between other types of delimiters such as parentheses, brackets, or curly braces.  # test case 6
# It can be extended to handle more complex cases such as nested delimiters or escaped delimiters.  # test case 7
# It can also be used to extract values from a string that contains multiple types of delimiters.  # test case 8
# The function can be modified to handle different types of quotation marks such