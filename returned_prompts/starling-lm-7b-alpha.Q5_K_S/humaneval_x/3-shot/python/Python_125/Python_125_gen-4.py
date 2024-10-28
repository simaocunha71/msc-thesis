    def split_words(txt):
        words = txt.split(' ')
        if len(words) == 0:
            return len([i for i in txt if ord(i) % 2 == 1 and ord(i) - ord('a') > 0])
        elif txt.find(',') > -1:
            return txt.split(',')
        else:
            return len([i for i in txt if ord(i) % 2 == 1 and ord(i) - ord('a') > 0])


