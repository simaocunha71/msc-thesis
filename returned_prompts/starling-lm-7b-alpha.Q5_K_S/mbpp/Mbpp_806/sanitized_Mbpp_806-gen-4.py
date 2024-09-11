def max_run_uppercase(string):
    # Initialize max_run_uppercase
    max_run_uppercase = 0
    # Initialize current_run_uppercase
    current_run_uppercase = 0
    # Iterate through each character in the string
    for char in string:
        if char.isupper():
            current_run_uppercase += 1
        else:
            # If a non-uppercase character is found, compare and update max_run_uppercase
            max_run_uppercase = max(max_run_uppercase, current_run_uppercase)
            # Reset current_run_uppercase
            current_run_uppercase = 0
    # Compare and update max_run_uppercase one final time
    max_run_uppercase = max(max_run_uppercase, current_run_uppercase)
    return max_run_uppercase