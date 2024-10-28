    def sort_even(l: list):
        even_index = [i for i in range(len(l)) if i % 2 == 0]
        return [l[i] if i % 2 == 1 else l[i] for i in even_index] + \
               [l[i] if i % 2 == 0 else l[i] for i in even_index]


