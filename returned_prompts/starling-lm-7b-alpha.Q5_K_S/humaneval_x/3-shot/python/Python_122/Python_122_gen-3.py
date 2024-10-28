    def add_elements(arr, k):
        return sum(arr[:k] if len(arr[:k]) > 2 else arr[:2])


