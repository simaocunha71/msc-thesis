# Here's a step-by-step breakdown of the solution:

# Step 1: Create a function called total_match that takes in two parameters, lst1 and lst2.
# Step 2: Initialize an empty list called result to store the result.
# Step 3: Calculate the total number of characters in lst1 by using the sum() function and the length operator (len()) on each string in the list. Add this value to a variable called lst1_chars.
# Step 4: Calculate the total number of characters in lst2 using the same method as step 3, and store the result in a variable called lst2_chars.
# Step 5: Compare the values of lst1_chars and lst2_chars. If lst1_chars is less than lst2_chars, append all the strings in lst1 to the result list. Otherwise, append all the strings in lst2 to the result list.
# Step 6: Return the result list as the output of the function.

def total_match(lst1, lst2):
    result = []
    lst1_chars = sum(len(s) for s in lst1)
    lst2_chars = sum(len(s) for s in lst2)
    
    if lst1_chars < lst2_chars:
        result = lst1
    else:
        result = lst2
        
    return result

# Here are some test cases to verify the correctness of the solution:
print(total_match([], []))  # Expected output: []
print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # Expected output: ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # Expected output: ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # Expected output: ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # Expected output: ['4']

# The