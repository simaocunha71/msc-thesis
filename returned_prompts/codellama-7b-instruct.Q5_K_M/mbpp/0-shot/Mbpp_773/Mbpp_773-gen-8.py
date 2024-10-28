def occurance_substring(string, substring):
    start_index = string.find(substring)
    if start_index == -1:
        return None
    else:
        return substring, start_index, start_index + len(substring)

# Example:
# In [1]: occurance_substring('python programming, python language','python')
# Out[1]: ('python', 0, 6)
