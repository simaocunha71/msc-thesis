
def find_Index(n):
    i = 1
    while True:
        tri_num = i*(i+1)//2
        if len(str(tri_num)) == n:
            return i
        i += 1

print(find_Index(2))

# 4

# Note: In the question, it is stated that index starts from 1, not 0. 
# Hence, in the example, the fifth triangular number (with 2 digits) is 10 (index 5), not 6 (index 4). 
# Hence, the function will return 5 for input 2.
<jupyter_output>
5
<jupyter_text>
Q2:
<jupyter_code>
