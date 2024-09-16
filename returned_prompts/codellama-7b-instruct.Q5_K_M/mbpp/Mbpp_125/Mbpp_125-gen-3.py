"""
def find_length(binary_string):
    count = 0
    max_length = 0
    for char in binary_string:
        if char == "1":
            count += 1
        else:
            count = 0
        max_length = max(max_length, count)
    return max_length
"""
