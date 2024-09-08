def sort_numeric_strings(lst):
    return sorted(int(num) for num in lst)

print(sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500']))


"""
This function works by using a generator expression to convert each string in the list to an integer, then using the sorted function to sort these integers. The sorted function returns a new list that contains all the numbers from the input list in ascending order.
"""
<jupyter_output>
[-500, -12, 0, 4, 7, 12, 45, 100, 200]
<jupyter_text>
Exercise 2
<jupyter_code>
