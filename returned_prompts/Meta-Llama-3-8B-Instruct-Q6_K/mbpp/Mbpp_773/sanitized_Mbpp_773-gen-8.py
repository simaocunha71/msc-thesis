def occurance_substring(text, sub):
    try:
        start = text.index(sub)
        return (sub, start, start + len(sub))
    except ValueError:
        return None