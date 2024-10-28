def first_repeated_char(s):
    # initialize an empty set to store seen characters
    seen = set()

    # iterate over each character in the string
    for ch in s:
        # if the character is in the set, return it
        if ch in seen:
            return ch
        # otherwise, add it to the set
        else:
            seen.add(ch)

    # if no repeated characters, return None
    return None