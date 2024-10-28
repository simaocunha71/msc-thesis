def count_Substrings(s):
    def check(s):
        digits = [int(i) for i in s]
        return sum(digits) == len(digits)
    return sum(1 for i in range(len(s)) for j in range(i, len(s)) if check(s[i:j+1]))