
def will_it_fly(q, w):
    return q == q[::-1] and sum(q) <= w

print(will_it_fly([1, 2], 5))
print(will_it_fly([3, 2, 3], 1))
print(will_it_fly([3, 2, 3], 9))
print(will_it_fly([3], 5))
<jupyter_output>
False
False
True
True
<jupyter_text>
Question 2:
<jupyter_code>
