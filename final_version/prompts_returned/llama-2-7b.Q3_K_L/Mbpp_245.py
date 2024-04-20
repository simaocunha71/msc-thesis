"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""
def findMaxSumBitonic(arr):
    n = len(arr)

    def bitonic_seq(i):
        if i < 0 or i >= n: return []
        if arr[i] > arr[i+1]:
            return [arr[i]] + bitonic_seq(i - 1)
        else:
            return [arr[i]] + bitonic_seq(i)

    def max_sum(seq):
        n = len(seq)

        def subsequence_max_sum(j, i):
            if j == n-1 or i < 0: return 0
            if seq[j][i] > seq[j+1][i]:
                return max(subsequence_max_sum(j - 1, i) + seq[j][i], subsequence_max_sum(j, i-1))
            else:
                return max(subsequence_max_sum(j, i-1), subsequence_max_sum(j+1, i))
        return subsequence_max_sum(n - 1, n)

    return max_sum(bitonic_seq(0))

print('max sum is: ', findMaxSumBitonic([5, 6, 7, 9]))