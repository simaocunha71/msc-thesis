    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])  # or: ''.join([char for char in text if char.lower() not in 'aeiou'])  # ignore case


