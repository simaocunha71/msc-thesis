"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""
import re

def is_decimal(s):
    pattern = r'(^\d+(\.\d{1,4})?)$'
    
    try:
        match = re.search(pattern, s)
        
        if not match or len(match.group(0)) == 0: return False
        dec_num = float(''.join([c for c in match[0] if ord(c) >= 48 and ord(c) <= 57]))
        
        while True:
            dec_num += .1
            
            if not s.isdigit(): break
            
            if s == str(dec_num): return True
    except ValueError as exc:
        return False
    
print(is_decimal('123.0'))