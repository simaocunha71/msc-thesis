def reverse_vowels(word):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    word_list = list(word)
    for i in range(len(word_list)):
        if word_list[i] in vowel:
            word_list[i] = vowel[vowel.index(word_list[i]) - 1]
    return ''.join(word_list)