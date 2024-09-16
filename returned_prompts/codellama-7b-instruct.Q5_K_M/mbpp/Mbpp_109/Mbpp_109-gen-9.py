"""
def odd_Equivalent(binary_string,num_rotations):
    binary_string = list(binary_string)
    for i in range(num_rotations):
        binary_string.append(binary_string.pop(0))
    count = 0
    for i in binary_string:
        if i == "1":
            count += 1
    return count
"""
