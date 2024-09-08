
def pair_xor_Sum(arr, n):
    sum = 0
    for i in range(0, 32):
        c = 0
        for j in range(0, n):
            if ((arr[j] >> i) & 1):
                c += 1
        sum += c * (n - c) * 2
    return sum


print(pair_xor_Sum([5,9,7,6],4))
<jupyter_output>
47
<jupyter_text>
