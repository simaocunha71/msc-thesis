    words = s.split()
    apple_count = 0
    for word in words:
        if word.endswith('apples'):
            apple_count = int(word.split(' ')[0])
        elif word.endswith('oranges'):
            orange_count = int(word.split(' ')[0])
    return n - apple_count - orange_count


