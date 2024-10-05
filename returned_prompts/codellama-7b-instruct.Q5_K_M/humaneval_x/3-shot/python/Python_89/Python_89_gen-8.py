    s = s.lower()
    result = ""

    for i in s:
        if i.isalpha():
            if i.isupper():
                if (ord(i) - ord('a') + 2) > ord('z'):
                    result += chr((ord(i) - ord('a') + 2) - 26)
                else:
                    result += chr(ord(i) - ord('a') + 2)

            else:
                if (ord(i) - ord('a') + 2) > ord('z'):
                    result += chr((ord(i) - ord('a') + 2) - 26)
                else:
                    result += chr(ord(i) - ord('a') + 2)

        else:
            result += i

    return result


