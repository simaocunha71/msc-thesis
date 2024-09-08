def freq_count(lst):
    freqs = {}
    for i in lst:
        if i in freqs:
            freqs[i] += 1
        else:
            freqs[i] = 1
    return freqs

print(freq_fre([10,10,10,10,20,20,20,20,40,40,50,50,30]))
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
