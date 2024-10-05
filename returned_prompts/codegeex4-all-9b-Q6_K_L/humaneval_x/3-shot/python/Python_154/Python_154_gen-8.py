    def rotate(word):
        return word[-1] + word[:-1]

    return b in a or b in rotate(a) or b in rotate(rotate(a)) or b in rotate(rotate(rotate(a)))

