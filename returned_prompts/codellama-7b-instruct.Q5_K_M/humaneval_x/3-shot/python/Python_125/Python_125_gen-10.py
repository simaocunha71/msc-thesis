    if len(txt.split()) > 0:
        return txt.split()
    else:
        if len(txt.split(',')) > 0:
            return txt.split(',')
        else:
            count = 0
            for i in range(26):
                if txt.lower()[0] == chr(i):
                    count += 1
            return count


