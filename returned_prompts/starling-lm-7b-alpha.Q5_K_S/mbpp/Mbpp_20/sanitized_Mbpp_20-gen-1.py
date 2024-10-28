def is_woodall(n):
    # Step 2: Check if the number is less than 10
    if n < 10:
        return True

    # Step 3: Initialize an empty list to store the digits of the number
    lst = []
    # Convert the number to a string and iterate over each character
    for char in str(n):
        # Convert each character back to an integer and append it to the list
        lst.append(int(char))

    # Step 4: Initialize an empty list to store the sum of the digits in the list
    result = []
    # Iterate over each number in the list and add it to the result list
    for num in lst:
        result.append(num)

    # Step 5: Convert the result list to a string and join all the numbers in the list
    result_str = ''.join(map(str, result))
    # Check if the resulting string is equal to the original number
    if result_str == str(n):
        return True
    else:
        return False