
def count_upper(s):
    count = 0
    for i, letter in enumerate(s):
        if i % 2 == 0 and letter.isupper():
            count += 1
    return count
