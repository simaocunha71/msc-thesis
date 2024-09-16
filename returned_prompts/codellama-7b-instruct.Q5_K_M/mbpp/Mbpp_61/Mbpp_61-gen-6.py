"""
def count_Substrings(string):
    count = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if sum(int(digit) for digit in string[i:j+1]) == j+1:
                count += 1
    return count
"""
