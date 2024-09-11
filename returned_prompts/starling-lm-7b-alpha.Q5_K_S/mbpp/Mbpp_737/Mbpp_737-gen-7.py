"""
import re

def check_str(s):
    regex = r'^[aeiou]'
    return re.match(regex, s) is not None


"""

def check_str(s):
    return s[0] in 'aeiou'

def check_str(s):
    if s[0] in 'aeiou':
        return True
    else:
        return False


def check_str(s):
    return s[0].lower() in 'aeiou'

def check_str(s):
    if s[0].lower() in 'aeiou':
        return True
    else:
        return False


def check_str(s):
    return s[0].islower() and s[0] in 'aeiou'

def check_str(s):
    return s[0].lower() in 'aeiou'


def check_str(s):
    return s[0].lower() == s[0] and s[0] in 'aeiou'


def check_str(s):
    return s[0].lower() == s[0] and s[0] in 'aeiou'

def check_str(s):
    return s[0].lower() == s[0] and s[0] in 'aeiou'

def check_str(s):
    return s[0].lower() == s[0] and s[0] in 'aeiou'

def check_str(s):
    return s[0].lower() == s[0] and s[0] in 'aeiou'

def check_str(s):
    return s[0].lower() == s[0] and s[0] in 'aeiou'

def check_str(s):
    return s[0].lower() == s[0] and s[0] in 'aeiou'

def check_str(s):
    return s[0].lower() == s[0] and s[0] in 'aeiou'

def check_str(s):
    return s[0].lower() == s[0