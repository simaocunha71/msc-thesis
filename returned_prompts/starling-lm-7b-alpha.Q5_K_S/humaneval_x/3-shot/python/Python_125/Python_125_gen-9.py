    if not txt.find(' '):
        result = []
        for i in range(len(txt)):
            result.append(ord(txt[i]))
            if ord(txt[i]) % 2 != 0:
                result.pop()
        return result
    if not txt.find(','):
        return [chr(i) for i in range(ord('a'), ord('z') + 1) if i % 2 != 0]
    else:
        return txt.split(" ")


