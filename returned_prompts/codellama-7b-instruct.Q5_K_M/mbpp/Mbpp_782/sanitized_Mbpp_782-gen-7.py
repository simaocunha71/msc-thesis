def odd_length_sum(my_list):
    # Initialize a variable to store the sum
    total = 0
    # Loop through each element of the list
    for i in range(len(my_list)):
        # Find the sum of the elements between i and i + 1
        total += sum(my_list[i:i+1])
    return total