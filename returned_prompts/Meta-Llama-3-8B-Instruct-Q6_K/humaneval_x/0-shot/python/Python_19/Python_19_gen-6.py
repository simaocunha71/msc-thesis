    import re
    from functools import reduce

    def sort_numbers(numbers: str) -> str:
        # Convert the input string to a list of numbers
        num_list = re.findall(r'\w+', numbers)

        # Define a dictionary to map words to their corresponding integer values
        num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

        # Use a lambda function to convert the list of words to a list of integers
        num_list = list(map(lambda x: num_dict[x], num_list))

        # Use the reduce function to sort the list of numbers
        num_list.sort()

        # Convert the list of integers back to a list of words
        num_list = list(map(lambda x: list(num_dict.keys())[list(num_dict.values()).index(x)], num_list))

        # Join the list of words into a string
        sorted_numbers = ' '.join(num_list)

        return sorted_numbers

    # Example usage
    print(sort_numbers('three one five'))  # Output: 'one three five'
    print(sort_numbers('nine eight seven'))  # Output: 'seven eight nine'
    print(sort_numbers('zero five four'))  # Output: 'four five zero'







