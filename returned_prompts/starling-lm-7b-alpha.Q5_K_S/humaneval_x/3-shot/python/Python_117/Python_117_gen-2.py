    def is_consonant(char):
        return char not in "aeiou"

    def select_words_helper(s, n, acc, idx):
        if idx == len(s):
            if n == 0:
                acc.append("".join(s))
            return

        select_words_helper(s, n, acc, idx + 1)
        if is_consonant(s[idx]) and n > 0:
            n -= 1
            select_words_helper(s, n, acc, idx + 1)

    select_words_helper(s, n, [], 0)
    return acc


