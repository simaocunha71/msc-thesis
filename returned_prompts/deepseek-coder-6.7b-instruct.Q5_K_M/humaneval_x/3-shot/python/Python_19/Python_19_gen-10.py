    num_to_word = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    word_to_num = {v: k for k, v in num_to_word.items()}

    numbers_as_nums = [num_to_word[num] for num in numbers.split()]
    numbers_as_nums.sort()

    return ' '.join(word_to_num[num] for num in numbers_as_nums)


