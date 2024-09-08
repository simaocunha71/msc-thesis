def find_star_num(n):
    def star(n):
        if n == 1:
            return 1
        elif n == 2:
            return 13
        else:
            return 2 * star(n - 1) + 3 * star(n - 2) + 1

    return star(n)