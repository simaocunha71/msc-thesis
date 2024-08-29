def test_three_equal(a, b, c):
    if a==b==c:
        return 3
    elif a==b or a==c or b==c:
        return 2
    else:
        return 0

print(test_three_equal(1,1,1))
print(test_three_equal(1,2,1))
print(test_three_equal(1,2,3))
print(test_three_equal(3,3,3))
print(test_three_equal(1,1,2))
<jupyter_output>
3
2
0
3
2
<jupyter_text>
Question 6
<jupyter_code>
