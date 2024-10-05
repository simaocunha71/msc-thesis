    vowels = 'aeiouAEIOU'
    return ''.join([c for c in text if c not in vowels])  # list comprehension to filter out vowels


