def find_Index(n):
    i = 1
    while True:
        triangular_num = i*(i+1)//2
        if len(str(triangular_num)) == n:
            return i
        i += 1
print(find_Index(2))
<jupyter_output>
4
<jupyter_text>
Problem 3
<jupyter_code>
