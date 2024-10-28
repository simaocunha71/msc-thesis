
def search(lst):
    # Step 1: Initialize a dictionary to keep track of the frequency of each number
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    # Step 2: Initialize a variable to keep track of the maximum number
    max_num = -1
    # Step 3: Loop through the list and compare each number with the current maximum number
    #         If the number is greater than the current maximum number, and the frequency of the number is greater than or equal to the value of the number itself, then update the maximum number
    for num in lst:
        if num > max_num and freq[num] >= num:
            max_num = num
    # Step 4: If no such a value exist, return -1
    if max_num == -1:
        return -1
    # Step 5: Return the maximum number
    return max_num
