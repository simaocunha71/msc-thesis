def digitSum(s):
    total = 0
    for letter in s:
        if letter.isupper():
            total += ord(letter)
    return total


