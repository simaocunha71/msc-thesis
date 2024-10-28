
def count_upper(s):
    count = 0
    for i, char in enumerate(s):
        if i % 2 == 0 and char.isupper():
            count += 1
    return count
