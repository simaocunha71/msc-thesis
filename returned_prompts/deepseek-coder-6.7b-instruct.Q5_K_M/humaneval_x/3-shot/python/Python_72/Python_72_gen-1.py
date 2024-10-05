    def is_balanced(q):
        return q == q[::-1]

    return is_balanced(q) and sum(q) <= w

