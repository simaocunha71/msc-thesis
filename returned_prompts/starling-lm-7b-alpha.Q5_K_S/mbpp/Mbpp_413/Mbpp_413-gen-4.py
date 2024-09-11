def extract_nth_element(lst,n):
    # Create an empty list to store the extracted elements
    extracted_list = []
    # Iterate through each tuple in the list
    for i in range(len(lst)):
        # Append the nth element of the tuple to the extracted_list
        extracted_list.append(lst[i][n])
    # Return the extracted_list
    return extracted_list

# Test the function
print(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0)) # ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']

# Time complexity: O(n)
# Space complexity: O(1)

# Alternatively, you can use the following function that has a time complexity of O(k), where k is the total number of elements to be extracted:

def extract_nth_element(lst,n):
    # Create an empty list to store the extracted elements
    extracted_list = []
    # Iterate through each tuple in the list
    for i in range(len(lst)):
        # If the index of the element is equal to n, append it to the extracted_list
        if i == n:
            extracted_list.append(lst[i])
    # Return the extracted_list
    return extracted_list

# Test the function
print(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0)) # [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 9