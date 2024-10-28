    words = txt.split()

    if len(words) > 0:
        return words
    else:
        count = 0
        for i in range(ord('a'), ord('z') + 1):
            if txt.lower().count(chr(i)) % 2 == 1:
                count += 1
        return count


