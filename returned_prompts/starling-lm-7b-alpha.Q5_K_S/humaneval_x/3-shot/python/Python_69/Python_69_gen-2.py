    from collections import Counter
    def search(lst):
        freq = Counter(lst)
        for elem in freq:
            if freq[elem] >= elem:
                return elem
        return -1


