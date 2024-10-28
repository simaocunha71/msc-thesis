    def sort_third(l: list):
        third_index = [i for i,x in enumerate(l) if i % 3 == 0]
        return [l[i] if i not in third_index else sorted(l)[i] for i in range(len(l))]


