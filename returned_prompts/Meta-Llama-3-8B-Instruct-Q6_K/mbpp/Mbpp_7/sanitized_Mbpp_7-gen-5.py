def find_char_long(s):
    words = s.split()
    return set(word for word in words if len(word) >= 4)  # or set(word for word in words if len(word) > 3) if you want to include words of exactly 4 characters long