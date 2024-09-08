def test_three_equal(num1, num2, num3):
    if num1==num2==num3:
        return 3
    elif num1==num2 or num1==num3 or num2==num3:
        return 2
    else:
        return 0

print(test_three_equal(1,1,1)) # should return 3
print(test_three_equal(1,2,3)) # should return 0
print(test_three_equal(1,1,2)) # should return 2
print(test_three_equal(1,2,1)) # should return 2
print(test_three_equal(2,2,1)) # should return 2
print(test_three_equal(2,1,1)) # should return 2
print(test_three_equal(2,2,2)) # should return 3
<jupyter_output>
3
0
2
2
2
2
3
<jupyter_text>
Question 2
<jupyter_code>
