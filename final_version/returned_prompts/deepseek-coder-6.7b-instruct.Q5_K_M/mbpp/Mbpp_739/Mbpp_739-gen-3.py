
def find_Index(n):
    i = 1
    while True:
        tri_num = i*(i+1)//2
        if len(str(tri_num)) == n:
            return i
        i += 1

print(find_Index(2))

# 4
<jupyter_output>
4
<jupyter_text>
