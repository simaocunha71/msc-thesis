
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    if (x_num * n_num) % x_denom == 0 and (x_num * n_num) % x_denom == 0:
        return True
    else:
        return False

# Test cases
print(simplify("1/5", "5/1")) # True
print(simplify("1/6", "2/1")) # False
print(simplify("7/10", "10/2")) # False

# Output:
# True
# False
# False
<jupyter_output>
True
False
False
<jupyter_text>
Question 2
<jupyter_code>
