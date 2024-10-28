    words = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

    def wordify(n):
        if n >= 1 and n <= 9:
            return words[n]
        else:
            return ""

    return [wordify(n) for n in sorted([n for n in arr if n >= 1 and n <= 9])[::-1]]

