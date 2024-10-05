    return len([i for i in range(len(string)) if string[i:].startswith(substring)])  # or use string.count(substring) for non-overlapping count


