    def swap_case(s):
        """
        Swap case of a given string
        """
        return s.swapcase()

    def replace_vowels(s):
        """
        Replace vowels with the letter that appears 2 places ahead of that vowel in the english alphabet
        """
        result = ""
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(s)):
            if s[i].lower() in vowels:
                result += vowels[(vowels.index(s[i].lower()) + 2) % 5]
            else:
                result += s[i]
        return result

    return replace_vowels(swap_case(message))


