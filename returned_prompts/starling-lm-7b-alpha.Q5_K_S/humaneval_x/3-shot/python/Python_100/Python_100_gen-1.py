    def make_a_pile_helper(n):
        if n % 2 == 0:
            return [n] + make_a_pile_helper(n+2)
        return [n] + make_a_pile_helper(n+1)

    return make_a_pile_helper(n)


