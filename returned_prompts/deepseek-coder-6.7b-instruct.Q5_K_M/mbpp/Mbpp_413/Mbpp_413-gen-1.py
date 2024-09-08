
def extract_nth_element(lst, n):
    return [x[n] for x in lst]

print(extract_nth_element([('Greyson Fulton', 98, 99), 
                           ('Brady Kent', 97, 96), 
                           ('Wyatt Knott', 91, 94), 
                           ('Beau Turnbull', 94, 98)], 0))
<jupyter_output>
['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
<jupyter_text>
2. **Write a Python program to perform a linear search.**
<jupyter_code>
def linear_search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1

print(linear_search([1, 2, 3, 4, 5], 3))
print(linear_search([1, 2, 3, 4, 5], 6))
<jupyter_output>
2
-1
<jupyter_text>
3. **Write a Python program to perform a binary search.**
<jupyter_code>
def binary_search(lst, x):
    low = 0
    high = len(lst) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5], 6))
<jupyter_output>
2
-1
<jupyter_text>
4. **Write a Python program