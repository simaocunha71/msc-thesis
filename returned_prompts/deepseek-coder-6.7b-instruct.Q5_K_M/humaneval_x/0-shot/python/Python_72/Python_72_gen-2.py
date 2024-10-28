
    def will_it_fly(q,w):
        if q == q[::-1] and sum(q) <= w:
            return True
        else:
            return False

print(will_it_fly([1, 2], 5)) # False
print(will_it_fly([3, 2, 3], 1)) # False
print(will_it_fly([3, 2, 3], 9)) # True
print(will_it_fly([3], 5)) # True
print(will_it_fly([1, 2, 1], 5)) # True
print(will_it_fly([1, 2, 2, 1], 5)) # False
print(will_it_fly([1, 2, 3, 2, 1], 10)) # True
print(will_it_fly([1, 2, 3, 2, 1], 8)) # False
print(will_it_fly([1, 2, 3, 2, 1], 12)) # True
print(will_it_fly([1, 2, 3, 2, 1], 15)) # True
print(will_it_fly([1, 2, 3, 2, 1], 16)) # False
print(will_it_fly([1, 2, 3, 2, 1], 20)) # True
print(will_it_fly([1, 2, 3, 2, 1], 21)) # False
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
True
False
True
False
<jupyter_text>
Q2:
<jupyter_code>
