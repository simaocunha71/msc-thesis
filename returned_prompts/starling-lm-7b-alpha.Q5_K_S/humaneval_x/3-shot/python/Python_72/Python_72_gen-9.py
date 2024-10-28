    def will_it_fly(q, w):
        if w == 0:
            return False
        if w == 1:
            return True
        if len(q) == 0:
            return False
        if len(q) == 1:
            return w >= q[0]
        if len(q) % 2 == 1:
            return False
        mid = len(q) // 2
        return (will_it_fly(q[:mid], w) and
                will_it_fly(q[mid:], w))


