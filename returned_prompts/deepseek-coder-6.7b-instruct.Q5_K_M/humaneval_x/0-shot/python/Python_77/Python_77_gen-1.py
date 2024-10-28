
def iscube(a):
    x = round(a ** (1. / 3))
    return x * x * x == a

print(iscube(1))
print(iscube(2))
print(iscube(-1))
print(iscube(64))
print(iscube(0))
print(iscube(180))
<jupyter_output>
True
False
True
True
True
False
<jupyter_text>
Problem 8
<jupyter_code>
