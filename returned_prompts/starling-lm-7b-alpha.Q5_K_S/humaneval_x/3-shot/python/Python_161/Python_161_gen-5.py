    result = ""
    for i in s:
        if i.isalpha():
            result += chr(ord(i) - (ord('a') - ord('A'))) if i.islower() else chr(ord(i) + (ord('a') - ord('A')))
        else:
            result += i
    return result[::-1]


