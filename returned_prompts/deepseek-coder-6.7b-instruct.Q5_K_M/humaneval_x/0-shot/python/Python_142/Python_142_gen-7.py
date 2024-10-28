


    sum_lst = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            sum_lst += lst[i]**2
        elif i % 4 == 0:
            sum_lst += lst[i]**3
        else:
            sum_lst += lst[i]
    return sum_lst
<jupyter_output>
<empty_output>
<jupyter_text>
The function sum_squares(lst) works by iterating over the given list lst. It checks if the index of the current element is divisible by 3 or 4. If it's divisible by 3, it squares the element and adds it to the sum. If it's divisible by 4 but not by 3, it cubes the element and adds it to the sum. If it's neither divisible by 3 nor by 4, it just adds the element to the sum. At the end, it returns the sum.
<jupyter_code>
print(sum_squares([1,2,3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1,-5,2,-1,-5]))  # Output: -126
<jupyter_output>
6
0
-126
<jupyter_text>
Problem 3: (5 points)Write a function called `sort_by_last_two_digits` that takes a list of integers as input, and returns a new list with the same integers sorted by their last two digits. The digits of the integers are considered in base 10. If two integers have the same last two digits, they should be ordered in the same order as they appeared in the input list.You can assume that the input list will only contain positive integers.
<jupyter_code>
