def max_sum_increasing_subseq(seq, i, k):
    dp = [0] * len(seq)
    for i in range(len(seq)):
        if i > 0:
            dp[i] = max(dp[i], dp[i-1] + seq[i])
        else:
            dp[i] = seq[i]
    return dp[k-1]

# print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4))
# print(max_sum_increasing_subseq([1, 2, 3, 4, 5], 1, 3))
# print(max_sum_increasing_subseq([1, 2, 3, 4, 5], 1, 5))
# print(max_sum_increasing_subseq([1, 2, 3, 4, 5], 4, 5))
# print(max_sum_increasing_subseq([1, 2, 3, 4, 5], 4, 4))
# print(max_sum_increasing_subseq([1, 2, 3, 4, 5], 1, 1))
# print(max_sum_increasing_subseq([1, 2, 3, 4, 5], 2, 2))
# print(max_sum_increasing_subseq([1, 2, 3, 4, 5], 2, 3))
# print(max_sum_increasing_subseq([1, 2, 3, 4, 5], 3, 3))
# print(max_sum_increasing_subseq([1, 2, 3, 4, 5], 3, 4))
# print(max_sum_increasing_subseq([1, 2, 3, 4, 5], 4, 4))
# print(max_sum_increasing_subseq([1, 2