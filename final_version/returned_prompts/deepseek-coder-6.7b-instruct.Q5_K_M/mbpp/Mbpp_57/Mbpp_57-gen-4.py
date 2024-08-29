def find_Max_Num(lst):
    str_nums = [str(i) for i in lst]
    str_nums.sort(reverse=True)
    return int(''.join(str_nums))

print(find_Max_Num([1,2,3])) # Expected output: 321

Explanation:
This python function works by converting each of the digits in the list to a string, then sorting the list in reverse order. This places the largest possible number at the start of the list (since the largest possible number would be the first item in a sorted list in descending order). Finally, it joins the strings together into a single string and converts this string back to an integer.
"""

