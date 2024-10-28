import re
def find_literals(string, regex):
    match = re.search(regex, string)
    return (match.group(0), match.start(), match.end())