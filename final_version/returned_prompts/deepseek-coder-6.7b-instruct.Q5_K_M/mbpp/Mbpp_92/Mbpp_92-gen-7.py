"""
def is_undulating(n):
    digits = [int(d) for d in str(n)]
    for i in range(len(digits)-2):
        if digits[i] == digits[i+1] or digits[i+1] == digits[i+2]:
            return False
    return True
"""

# Question 3
