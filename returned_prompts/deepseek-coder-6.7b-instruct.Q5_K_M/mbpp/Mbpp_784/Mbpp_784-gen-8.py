
def mul_even_odd(lst):
    even_num = 1
    odd_num = 1
    for num in lst:
        if num % 2 == 0:
            even_num *= num
        else:
            odd_num *= num
    return even_num, odd_num

print(mul_even_odd([1,3,5,7,4,1,6,8]))

#Output: (8, 168)

#Explanation:
#In the given list [1,3,5,7,4,1,6,8], even numbers are 4 and 6 and odd numbers are 1, 3, 5, 7, 1 and 8.
#Product of all even numbers 4 and 6 is 8 and product of all odd numbers 1, 3, 5, 7, 1 and 8 is 168. So, the output is (8, 168).
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4
<jupyter_code>
