def find_remainder(arr, n):
    product = 1
    for num in arr:
        product = (product * num) % n
    return product

print(find_remainder([ 100, 10, 5, 25, 35, 14 ],11))
<jupyter_output>
9
<jupyter_text>
Problem 3
<jupyter_code>
