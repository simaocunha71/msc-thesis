def find_literals(s, pattern):
    m = re.search(pattern, s)
    if m:
        return (m.group(0), m.start(), m.end())