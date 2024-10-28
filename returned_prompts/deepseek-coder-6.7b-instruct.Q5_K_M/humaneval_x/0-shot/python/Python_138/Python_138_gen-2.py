
    if n < 8:
        return False
    else:
        return True

print(is_equal_to_sum_even(4))
print(is_equal_to_sum_even(6))
print(is_equal_to_sum_even(8))

# Given number n is 4. It is less than 8, so the function returns False.
# Given number n is 6. It is less than 8, so the function returns False.
# Given number n is 8. It is equal to 8, so the function returns True.
<jupyter_output>
False
False
True
<jupyter_text>
Question 2: The following code will print the numbers from 0 to 9:
<jupyter_code>
for i in range(10):
    print(i)
<jupyter_output>
0
1
2
3
4
5
6
7
8
9
<jupyter_text>
Question 3: The following code will print the numbers from 0 to 19:
<jupyter_code>
for i in range(20):
    print(i)
<jupyter_output>
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
<jupyter_text>
Question 4: The following code will print the even numbers from 0 to 10:
<jupyter_code>
for i in range(11):
    if i % 2 == 0:
        print(i)
<jupyter_output>
0
2
4
6
8
10
<jupyter_text>
Question 5: The following code will print the square of each number in a list:
<jupyter_code>
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i**2)
<jupyter_output>
1
4
9
