
    def eat(number, need, remaining):
        if (remaining - number) >= need:
            return [number + need, remaining - need]
        else:
            return [number + remaining, 0]
