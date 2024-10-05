    return len([i for i in range(len(string)) if string[i:i+len(substring)] == substring])  # or use string.count(substring) for non-overlapping cases


