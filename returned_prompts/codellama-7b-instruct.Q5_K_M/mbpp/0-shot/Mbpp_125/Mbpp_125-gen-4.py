"""
def find_length(binary):
    max_diff = 0
    for i in range(len(binary)):
        count_0 = 0
        count_1 = 0
        for j in range(i, len(binary)):
            if binary[j] == "0":
                count_0 += 1
            else:
                count_1 += 1
            max_diff = max(max_diff, count_0 - count_1)
    return max_diff
"""

