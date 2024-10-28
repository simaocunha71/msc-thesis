    def will_it_fly(q, w):
        if sum(q) > w:
            return False
        else:
            return q == list(reversed(q)) and w >= sum(q)


