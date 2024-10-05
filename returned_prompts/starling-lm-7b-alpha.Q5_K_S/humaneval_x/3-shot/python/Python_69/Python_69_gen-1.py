    from collections import Counter

    def search(lst):
        c = Counter(lst)
        for num in reversed(lst):
            if c[num] >= num:
                return num
        return -1


