    def will_it_fly(q, w):
        if str(q) != str(q)[::-1]:
            return False
        return sum(q) <= w


