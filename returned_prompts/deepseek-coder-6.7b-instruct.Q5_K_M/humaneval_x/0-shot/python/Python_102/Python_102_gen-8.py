
    def choose_num(x, y):
        if x > y:
            return -1
        else:
            if x % 2 == 0 and x >= y:
                return x
            elif y % 2 == 0:
                return y
            else:
                return y - 1

print(choose_num(12, 15)) # 14
print(choose_num(13, 12)) # -1
print(choose_num(14, 15)) # 14
print(choose_num(15, 16)) # 16
print(choose_num(9, 11)) # -1
print(choose_num(13, 15)) # 14
<jupyter_output>
14
-1
14
16
-1
14
<jupyter_text>
Task 3:
<jupyter_code>
