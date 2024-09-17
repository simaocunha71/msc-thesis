def count_char_position(s: str) -> int:
    counter = 0
    for i in range(len(s)):
        if s[i].lower() == chr(ord('a')+i):
            counter += 1
    return counter

