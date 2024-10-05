    num_to_word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    word_to_num = {w: i for i, w in enumerate(num_to_word)}

    return ' '.join(sorted(numbers.split(), key=lambda x: word_to_num[x]))


