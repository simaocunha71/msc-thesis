def find_Max_Num(lst):
    lst = [str(i) for i in lst]
    lst.sort(reverse=True)
    return int(''.join(lst))

print(find_Max_Num([1,2,3])) # 321


"""
Explanation:
The function first converts all the numbers in the list into string format. Then it sorts the list in descending order. After that it joins all the strings in the list into a single string and converts it back to integer.
"""
<jupyter_output>
321
<jupyter_text>
Question 2
<jupyter_code>
