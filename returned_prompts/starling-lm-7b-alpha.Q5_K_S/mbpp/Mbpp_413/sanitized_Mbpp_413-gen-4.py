def extract_nth_element(lst,n):
    # Create an empty list to store the extracted elements
    extracted_list = []
    # Iterate through each tuple in the list
    for i in range(len(lst)):
        # Append the nth element of the tuple to the extracted_list
        extracted_list.append(lst[i][n])
    # Return the extracted_list
    return extracted_list