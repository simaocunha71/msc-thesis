def freq_count(lst):
    freqs = {}
    for i in lst:
        if i in freqs:
            freqs[i] += 1
        else:
            freqs[i] = 1
    return freqs

print(freq_fre([10,10,10,10,20,20,20,20,40,40,50,50,30]))

