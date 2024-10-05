    from collections import defaultdict

    def char_count(word):
        count = defaultdict(int)
        for char in word:
            count[char] += 1
        return count

    def max_word(words):
        max_count = 0
        max_word = ""
        for word in words:
            count = char_count(word)
            if len(count) > max_count:
                max_count = len(count)
                max_word = word
            elif len(count) == max_count:
                if word < max_word:
                    max_word = word
        return max_word

    return max_word


