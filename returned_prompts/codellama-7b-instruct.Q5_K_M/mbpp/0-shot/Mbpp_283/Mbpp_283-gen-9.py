def validate(n):
    digits = [int(i) for i in str(n)]
    freq = [digits.count(i) for i in digits]
    return all(freq[i] <= i for i in range(len(digits)))
