def test_three_equal(a,b,c):
    count = 0
    if a == b:
        count += 1
    if b == c:
        count += 1
    if c == a:
        count += 1
    return count

print(test_three_equal(1,1,1)) # 3
print(test_three_equal(1,2,3)) # 0
print(test_three_equal(1,1,2)) # 2
print(test_three_equal(2,2,2)) # 3
<jupyter_output>
3
0
2
3
<jupyter_text>
Question 2
<jupyter_code>
