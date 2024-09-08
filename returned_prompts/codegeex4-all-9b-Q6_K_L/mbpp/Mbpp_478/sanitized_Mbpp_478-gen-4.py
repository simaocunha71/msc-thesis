def remove_lowercase(s):
    def is_lower(s):
        return s.islower()
    return ''.join(s[i+1] if is_lower(s[i]) and is_lower(s[i+1]) else s[i] for i in range(len(s)-1)) + s[-1]