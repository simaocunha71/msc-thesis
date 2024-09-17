def extract_nth_element(tup_list, n):
    # Extract the nth element from each tuple in the list
    extracted_list = [tup[n] for tup in tup_list]
    return extracted_list