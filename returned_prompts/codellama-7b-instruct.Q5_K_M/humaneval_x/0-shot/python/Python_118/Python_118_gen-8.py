
    def get_closest_vowel(word):
        # Find the index of the last vowel in the word
        last_vowel_index = -1
        for i in range(len(word)-1, -1, -1):
            if word[i].lower() in 'aeiou':
                last_vowel_index = i
                break

        # If no vowel exists in the word
        if last_vowel_index == -1:
            return ''

        # Find the first consonant from the right side of the last vowel
        for i in range(len(word)-1, last_vowel_index, -1):
            if word[i].lower() not in 'aeiou':
                return word[i].upper()

        return ''
