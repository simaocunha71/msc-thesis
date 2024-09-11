def add_suffix_to_words(string, suffix):
    words = string.split()
    result = []
    for word in words:
        if word[-1] in ".,!?":
            result.append(word + suffix)
        else:
            result.append(word + '?' + suffix)
    return ' '.join(result)


"""
Write a function to find the longest common prefix among all the