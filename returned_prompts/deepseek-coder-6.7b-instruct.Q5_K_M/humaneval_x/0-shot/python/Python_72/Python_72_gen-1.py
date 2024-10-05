
def will_it_fly(q,w):
    if q == q[::-1] and sum(q) <= w:
        return True
    else:
        return False

print(will_it_fly([1, 2], 5)) # False
print(will_it_fly([3, 2, 3], 1)) # False
print(will_it_fly([3, 2, 3], 9)) # True
print(will_it_fly([3], 5)) # True
print(will_it_fly([1,2,1], 5)) # True
print(will_it_fly([1,2,1], 4)) # False
print(will_it_fly([1,1,1,1], 4)) # True
print(will_it_fly([1,1,1,1], 3)) # False
print(will_it_fly([1,2,2,1], 6)) # True
print(will_it_fly([1,2,2,1], 5)) # False
<jupyter_output>
False
False
True
True
True
False
True
False
True
False
<jupyter_text>
3. Write a Python program to find the area of a triangle given the base and height.
<jupyter_code>
