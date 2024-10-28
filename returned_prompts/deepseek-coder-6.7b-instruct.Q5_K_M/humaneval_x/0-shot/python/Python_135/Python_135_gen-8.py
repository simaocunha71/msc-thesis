
def can_arrange(arr):
    index = -1
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            index = i
            break
    return index

print(can_arrange([1,2,4,3,5]))  # 3
print(can_arrange([1,2,3]))  # -1
print(can_arrange([5,4,3,2,1]))  # 1
print(can_arrange([1,3,5,2,4]))  # 3
print(can_arrange([1]))  # -1
<jupyter_output>
3
-1
1
3
-1
<jupyter_text>
Problem 2:
<jupyter_code>
