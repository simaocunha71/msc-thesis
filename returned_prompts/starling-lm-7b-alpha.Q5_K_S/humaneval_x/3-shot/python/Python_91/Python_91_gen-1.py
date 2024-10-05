    count = 0
    for char in S:
        if char == '.' or char == '?' or char == '!':
            if S[count:count + 2] == "I ":
                count += 1
    return count


