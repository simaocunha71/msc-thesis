
def first_repeated_char(str):
    for ch in str:
        if str.count(ch) > 1:
            return ch


