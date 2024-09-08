def extract_values(s):
    # The findall function from the re module can be used to extract all substrings that match the provided regular expression.
    return re.findall(r'"([^"]*)"', s)