"""
def validate(n):
    digits = [int(d) for d in str(n)]
    return all(d <= digits.count(d) for d in digits)
"""

