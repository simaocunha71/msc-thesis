    vowels = set('aeiou')
    if s[-1] == 'y':
        vowels.add('y')
    return sum(1 for c in s if c in vowels)

