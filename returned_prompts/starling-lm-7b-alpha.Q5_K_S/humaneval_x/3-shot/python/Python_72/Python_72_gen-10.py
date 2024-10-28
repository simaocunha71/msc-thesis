    def will_it_fly(q, w):
        q_sum = sum(q)
        if q_sum > w:
            return False
        else:
            return q == q[::-1]


