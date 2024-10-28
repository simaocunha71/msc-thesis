
def vowels_count(s):
    # if 'y' is at the end of the string, count it as a vowel
    if s[-1] == 'y':
        return len([ch for ch in s if ch in 'aeiou'])
    else:
        return len([ch for ch in s if ch in 'aeiouy'])

