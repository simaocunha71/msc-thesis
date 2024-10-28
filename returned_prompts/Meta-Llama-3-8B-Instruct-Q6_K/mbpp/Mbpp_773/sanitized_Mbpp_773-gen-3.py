def occurance_substring(s, sub):
    try:
        start = 0
        while True:
            start = s.find(sub, start)
            if start == -1:
                return None
            yield (sub, start, start + len(sub))
            start += 1
    except ValueError:
        return None