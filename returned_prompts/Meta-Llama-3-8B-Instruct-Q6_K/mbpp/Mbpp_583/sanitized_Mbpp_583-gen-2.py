def catalan_number(n):
    if n <= 1:
        return 1
    catalan = [1] * (n + 1)
    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]
    return catalan[n] // (i + 1) if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]
    # else return catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n]  # divide by i+1 if i > 0 else catalan[n] 