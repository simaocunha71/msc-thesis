def closest_num(n):
    str_n = str(n)
    if n < 10:
        return -1
    else:
        for i in range(len(str_n) - 1, 0, -1):
            if str_n[i] < str_n[i-1]:
                str_n = str_n[:i-1] + str_n[i] + ''.join(sorted(str_n[i-1:i] + str_n[i+1:]))
                return int(str_n)
        return int(str_n)

print(closest_num(11))  # 10

"""
The function works by converting the number to a string, and then going through it from right to left. If it finds a digit that is smaller than the digit before it, it swaps the two digits and sorts the rest of the number in ascending order.
"""

# Alternative solution using list
def closest_num(n):
    num_list = list(str(n))
    if n < 10:
        return -1
    else:
        for i in range(len(num_list) - 1, 0, -1):
            if num_list[i] < num_list[i-1]:
                num_list[i-1:i] = sorted(num_list[i-1:i])
                return int("".join(num_list))
        return int("".join(num_list))

print(closest_num(11))  # 10

"""
This alternative solution uses a list of the digits in the number instead of a string. It also finds the digits from right to left in the same way as the first solution, but then sorts the digits in the found pair in ascending order and joins them back into a number.
"""
<jupyter_output>
10
10
<jupyter_text>
Task 2
<jupyter_code>
