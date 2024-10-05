    def has_even_digit(elem):
        for d in str(elem):
            if int(d) % 2 == 0:
                return True
        return False

    res = [elem for elem in x if not has_even_digit(elem)]
    res.sort()
    return res


