
    import re

    pattern = re.compile(r'[aeiou]')
    return pattern.sub('', text)


