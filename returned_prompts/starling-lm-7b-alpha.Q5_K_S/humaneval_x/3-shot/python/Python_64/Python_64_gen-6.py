    def vowels_count(s):
        vowel = "aeiouy"
        count = 0
        for i in s:
            if i in vowel:
                count += 1
        return count


