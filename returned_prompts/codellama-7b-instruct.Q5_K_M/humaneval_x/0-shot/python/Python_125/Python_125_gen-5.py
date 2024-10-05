
    def split_words(txt):
        txt = txt.split()
        if len(txt) == 0:
            return sum(i % 2 for i, c in enumerate(txt, start=1) if c.islower())
        else:
            return txt
