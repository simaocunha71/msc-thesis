    result = ''

    for word in sentence.split(' '):
        if len(word) % 2 == 1:
            result += word + ' '

    return result.strip()


