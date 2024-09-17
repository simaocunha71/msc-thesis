def extract_values(s):
    '''
    >>> extract_values('"Python", "PHP", "Java"')
    ['Python', 'PHP', 'Java']
    '''
    return [i[1:-1] for i in s.split('", "')]