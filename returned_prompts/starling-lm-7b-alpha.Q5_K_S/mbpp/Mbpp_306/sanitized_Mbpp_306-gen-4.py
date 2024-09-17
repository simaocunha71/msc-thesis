def max_sum_increasing_subseq(seq, i, k):
    dp = [0] * len(seq)
    for i in range(len(seq)):
        if i > 0:
            dp[i] = max(dp[i], dp[i-1] + seq[i])
        else:
            dp[i] = seq[i]
    return dp[k-1]