    def monotonic_helper(l: list) -> bool:
        if len(l) == 0 or len(l) == 1:
            return True
        last_elem = l[0]
        for elem in l[1:]:
            if elem > last_elem:
                return True
            elif elem < last_elem:
                return False
            last_elem = elem

        return True

    return monotonic_helper(l)


