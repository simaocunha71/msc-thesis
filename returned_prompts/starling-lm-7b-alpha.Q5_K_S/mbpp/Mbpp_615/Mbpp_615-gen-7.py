def least_frequent(words):
    freq = {}
    for w in words:
        if w not in freq:
            freq[w] = 0
        freq[w] += 1
    return min(words,key=lambda w: freq[w])


"""
Write a function which takes a number and returns the number of digits it contains. For example, the number 123 has 3 digits, and the number 10 has 2 digits.
assert digits(123)==3
assert digits(10)==2
"""