    def swap_case(s):
        return s.swapcase()

    def replace_vowels(s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i, vowel in enumerate(vowels):
            s = s.replace(vowel, chr(ord(vowel) + 2))
        return s

    return swap_case(replace_vowels(message))


