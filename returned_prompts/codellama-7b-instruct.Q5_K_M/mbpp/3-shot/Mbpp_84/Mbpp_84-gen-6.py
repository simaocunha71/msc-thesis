
def sequence(n: int) -> int:
    def newman_conway(n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return newman_conway(newman_conway(n-1)) + newman_conway(n-newman_conway(n-1))
    return newman_conway(n)


