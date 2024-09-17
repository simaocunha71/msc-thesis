import unittest
def extract_quotation(s):
    result = []
    start = 0
    for i in range(len(s)):
        if s[i] == '"':
            result.append(s[start+1:i])
            start = i + 1
    result.append(s[start:])
    return result