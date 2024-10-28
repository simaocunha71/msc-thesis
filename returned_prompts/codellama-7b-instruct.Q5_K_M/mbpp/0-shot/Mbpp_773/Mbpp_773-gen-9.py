def occurance_substring(string, substring):
    match = re.search(substring, string)
    if match:
        return match.group(0), match.start(), match.end()
    else:
        return None
