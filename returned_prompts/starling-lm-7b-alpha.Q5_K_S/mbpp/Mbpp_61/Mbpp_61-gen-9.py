
def count_Substrings(s: str):
    n = len(s)
    count = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += int(s[j])
            if curr_sum == j - i + 1:
                count += 1
    return count


