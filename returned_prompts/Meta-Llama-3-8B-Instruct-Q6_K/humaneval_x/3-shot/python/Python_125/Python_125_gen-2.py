    words = txt.split()
    if not words:
        return txt.replace(',', '').lower().count(chr(i) for i in range(ord('a'), ord('z')+1))
    else:
        return words


