    def split_words(txt):
        words = []
        if ' ' in txt:
            words = txt.split(' ')
        elif ',' in txt:
            words = txt.split(',')
        else:
            for i in range(len(txt)):
                if ord(txt[i]) % 2 != 0:
                    words.append(txt[i])

        return words


