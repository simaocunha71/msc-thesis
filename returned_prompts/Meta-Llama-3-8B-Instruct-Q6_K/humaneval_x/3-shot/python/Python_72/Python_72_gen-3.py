    def will_it_fly(q, w):
        if q == q[::-1]:
            return sum(q) <= w
        return False


