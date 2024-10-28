def is_decimal(s):
    if s.count('.') != 1:
        return False
    if s[:s.index('.')].isdigit() and s[s.index('.')+1:].isdigit() and s[s.index('.'):].count('0') <= 1:
        return True
    else:
        return False