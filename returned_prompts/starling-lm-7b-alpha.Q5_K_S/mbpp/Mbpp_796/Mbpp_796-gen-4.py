def is_empty(dictionary):
    if len(dictionary) == 0:
        return True
    else:
        return False

# Testing
assert is_empty({'a': 100, 'b':200, 'c':300}) == False
print("All Testing Passed")


"""
Write function to find the average value of all items in the given dictionary.
assert average_value({'a': 100, 'b':200, '