def odd_Equivalent(s, k):
    # Creating the equivalent binary strings
    bin_str = [s[i:] + s[:i] for i in range(len(s))]

    # Counting the odd binary strings
    odd_count = 0
    for i in bin_str:
        if int(i,2) % 2 == 1:
            odd_count +=1

    return odd_count