    def strange_sort(lst):
        result = []
        while lst:
            result.append(min(lst))
            lst = [x for x in lst if x != min(lst)]
        return result

    return strange_sort(lst)


