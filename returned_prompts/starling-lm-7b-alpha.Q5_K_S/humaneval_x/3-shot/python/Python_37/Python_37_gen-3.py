    def sort_even(l: list):
        sorted_even_indices = sorted(i for i in range(len(l)) if i % 2 == 0)
        return [l[i] if i % 2 != 0 else l[sorted_even_indices[i // 2]] for i in range(len(l))]


