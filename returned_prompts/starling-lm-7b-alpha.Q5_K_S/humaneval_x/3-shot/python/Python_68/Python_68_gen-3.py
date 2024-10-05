    def pluck(arr):
        smallest_even = None
        smallest_even_index = None
        for idx, elem in enumerate(arr):
            if elem % 2 == 0 and (smallest_even is None or elem < smallest_even):
                smallest_even = elem
                smallest_even_index = idx
        if smallest_even is None:
            return []
        return [smallest_even, smallest_even_index]


