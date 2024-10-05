
    hex_nums = ["2", "3", "5", "7", "B", "D"]
    return sum(hex_num in hex_nums for hex_num in num)

# Test cases:
print(hex_key("AB"))  # 1
print(hex_key("1077E"))  # 2
print(hex_key("ABED1A33"))  # 4
print(hex_key("123456789ABCDEF0"))  # 6
print(hex_key("2020"))  # 2
<jupyter_output>
1
2
4
6
2
<jupyter_text>
**Problem 2:**Write a function `hex_to_bin` that takes in a hexadecimal number as a string and returns its binary equivalent as a string.
<jupyter_code>
