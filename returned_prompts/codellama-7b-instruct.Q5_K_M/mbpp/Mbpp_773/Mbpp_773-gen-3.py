def occurance_substring(string, substring):
    occurrence = None
    if substring in string:
        occurrence = (substring, string.index(substring), string.index(substring)+len(substring))
    return occurrence



