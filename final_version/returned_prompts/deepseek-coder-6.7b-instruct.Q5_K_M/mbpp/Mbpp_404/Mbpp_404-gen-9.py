def minimum(a, b):
    if a <= b:
        return a
    else:
        return b

print(minimum(1,2))

#OR

def minimum(a, b):
    return a if a <= b else b

print(minimum(1,2))

#OR

def minimum(a, b):
    return min(a, b)

print(minimum(1,2))

#OR

print(min(1,2))

#OR

print((lambda a, b: a if a <= b else b)(1,2))

#OR

print((lambda a, b: min(a, b))(1,2))

#OR

print((lambda a, b: min(a, b))(1,2))

#OR

def minimum(*args):
    return min(args)

print(minimum(1,2))
<jupyter_output>
1
1
1
1
1
1
1
<jupyter_text>
Question 2:Write a Python function to find the maximum of two numbers.assert maximum(1,2) == 2
<jupyter_code>
