def find_literals(string, pattern):
    # Your code here
    import re
    return re.search(pattern, string).group(), re.search(pattern, string).start(), re.search(pattern, string).end()