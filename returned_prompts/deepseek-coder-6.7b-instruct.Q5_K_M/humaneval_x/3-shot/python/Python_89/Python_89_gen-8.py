    result = ''
    for c in s:
        if 'a' <= c <= 'z':
            result += chr(((ord(c) - ord('a') - 2) % 26) + ord('a'))
        elif 'A' <= c <= 'Z':
            result += chr(((ord(c) - ord('A') - 2) % 26) + ord('A'))
    return result


