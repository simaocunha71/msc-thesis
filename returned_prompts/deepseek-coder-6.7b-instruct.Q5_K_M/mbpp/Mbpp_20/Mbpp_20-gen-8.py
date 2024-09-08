
def is_woodall(n):
    if n < 10:
        return False
    else:
        digits = [int(d) for d in str(n)]
        return all(d != 0 and n % d == 0 for d in digits)

print(is_woodall(383))
<jupyter_output>
True
<jupyter_text>
Exercise 2:
<jupyter_code>
