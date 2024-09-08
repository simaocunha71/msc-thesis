def max_Product(arr):
    n = len(arr)
    arr.sort()
    if (arr[0] * arr[1]) > (arr[n - 1] * arr[n - 2]):
        return (arr[0], arr[1])
    else:
        return (arr[n - 1], arr[n - 2])

print(max_Product([1,2,3,4,7,0,8,4]))
<jupyter_output>
(7, 8)
<jupyter_text>
Question 2
<jupyter_code>
