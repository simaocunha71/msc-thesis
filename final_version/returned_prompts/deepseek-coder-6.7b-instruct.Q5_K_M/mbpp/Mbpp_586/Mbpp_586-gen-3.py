def split_Arr(arr, n):
    return arr[n:] + arr[:n]

print(split_Arr([12,10,5,6,52,36],2))

# OR

def split_Arr(arr, n):
    return arr[n+1:] + arr[:n+1]

print(split_Arr([12,10,5,6,52,36],2))

# OR

def split_Arr(arr, n):
    return arr[n:] + arr[:n]

print(split_Arr([12,10,5,6,52,36],2))
<jupyter_output>
[5, 6, 52, 36, 12, 10]
[5, 6, 52, 36, 12, 10]
[5, 6, 52, 36, 12, 10]
<jupyter_text>
**Question 3**
<jupyter_code>
