def odd_Equivalent(binary_string, rotation):
    odd_count = 0
    for i in range(len(binary_string)):
        rotated_string = binary_string[i:] + binary_string[:i]
        rotated_binary_string = rotated_string[-rotation:] + rotated_string[:-rotation]
        if int(rotated_binary_string, 2) % 2 != 0:
            odd_count += 1
    return odd_count

print(odd_Equivalent("011001",6))
<jupyter_output>
3
<jupyter_text>
Q2.Given an array of integers, find the shortest subarray which when sorted would make the entire array sorted.
<jupyter_code>
