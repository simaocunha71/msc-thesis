
    def prod_signs(arr):
        if not arr:
            return None
        prod = 1
        for num in arr:
            prod *= 1 if num > 0 else -1 if num < 0 else 0
        return sum(abs(num) for num in arr) * prod
