def extract_even(mixed_tuple):
    # Function to check if an item is an even number
    def is_even(n):
        return n % 2 == 0

    # Recursive function to process the tuple
    def process_tuple(t):
        result = []
        for item in t:
            # If item is a tuple, process it recursively
            if isinstance(item, tuple):
                processed_item = process_tuple(item)
                if processed_item:
                    result.append(processed_item)
            # If item is an even number, add it to the result
            elif is_even(item):
                result.append(item)
        return tuple(result)

    return process_tuple(mixed_tuple)