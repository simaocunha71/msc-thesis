    if not strings:
        return None

    return max(strings, key=len)  # Use max with key=len for the longest string


