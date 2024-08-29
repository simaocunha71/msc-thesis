def find_Odd_Pair(arr, n): 
    odd_count = 0
    for i in range(0, n): 
        if (arr[i] % 2 != 0): 
            odd_count += 1
    return odd_count * (odd_count - 1) // 2

print(find_Odd_Pair([5,4,7,2,1],5))
<jupyter_output>
6
<jupyter_text>
Question 2
<jupyter_code>
