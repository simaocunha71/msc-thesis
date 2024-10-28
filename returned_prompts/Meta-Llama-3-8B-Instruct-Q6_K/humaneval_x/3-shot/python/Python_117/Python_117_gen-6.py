    import re
    from collections import Counter

    def select_words(s, n):
        words = re.findall(r'\b\w+\b', s)
        result = []
        for word in words:
            counter = Counter(word.lower())
            if sum(counter[c] for c in 'bcdfghjklmnpqrstvwxyz') == n:
                result.append(word)
        return result


