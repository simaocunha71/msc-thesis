"""
import re

def is_decimal(s):
    if s.count('.') != 1:
        return False
    if s.startswith('.') or s.endswith('.'):
        return False
    if len(s) - s.count('.') - 1 > 3:
        return False
    return re.match(r'^\d*\.\d{2}$', s) is not None
"""
