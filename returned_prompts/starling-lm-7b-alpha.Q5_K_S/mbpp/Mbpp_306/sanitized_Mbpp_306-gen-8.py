def max_sum_increasing_subseq(seq, i, k):
    # Initialize the result
    result = [0] * len(seq)

    # Fill the result array
    result[i] = seq[i]
    for j in range(i + 1, len(seq)):
        if seq[j] > seq[j - 1]:
            result[j] = result[j - 1] + seq[j]
        else:
            result[j] = max(result[j - 1], seq[j])

    # Check if kth element is greater than ith element
    if seq[k - 1] > seq[i]:
        return result[k - 1]

    # Check if the sequence is increasing from ith element until kth element
    if seq[k - 1] > seq[k - 2]:
        return result[k - 1]

    # Check if the ith element is greater than kth element
    if seq[i] > seq[k - 1]:
        return result[i]

    # Return the maximum sum of the increasing subsequence until i
    return max(result[i], seq[k - 1])