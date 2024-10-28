def remove_uppercase(s):
    """
    Remove uppercase substrings from a given string.
    >>> remove_uppercase('cAstyoUrFavoRitETVshoWs')
    'cstyoravoitshos'
    """
    return ''.join(c for c in s if c.islower())