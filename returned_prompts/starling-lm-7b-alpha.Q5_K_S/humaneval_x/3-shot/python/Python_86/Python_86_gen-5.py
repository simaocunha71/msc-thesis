    def anti_shuffle(s):
        new_word = ""
        for char in s:
            new_word += chr(ord(char) - (ord('a') if char.islower() else ord('A') - 1))
        return new_word

    return " ".join(anti_shuffle(word) for word in s.split())


