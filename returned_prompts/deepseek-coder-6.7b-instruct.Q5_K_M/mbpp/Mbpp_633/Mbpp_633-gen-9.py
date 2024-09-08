def pair_xor_Sum(lst,n):
    res = 0
    for i in range(n):
        for j in range(i+1,n):
            res += lst[i]^lst[j]
    return res*2

print(pair_xor_Sum([5,9,7,6],4))

# This code works by iterating over all pairs of numbers in the list and calculating their XOR. The XOR of a pair is then added to a result variable. Since XOR is commutative (i.e., the order in which elements are XOR-ed does not affect the result), each pair is counted twice in the final result. Therefore, we multiply the result by 2 to get the correct answer.
<jupyter_output>
47
<jupyter_text>
Question 3
<jupyter_code>
