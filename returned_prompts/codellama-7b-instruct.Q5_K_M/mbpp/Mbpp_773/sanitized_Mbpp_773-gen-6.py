import re
def occurance_substring(input_string, substring):
    match = re.search(substring, input_string)
    if match:
        return (substring, match.start(), match.end())
    else:
        return None