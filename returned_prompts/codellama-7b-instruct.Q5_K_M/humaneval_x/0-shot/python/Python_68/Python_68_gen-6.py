
    def pluck(arr):
        result = []
        if not arr:
            return result
        smallest = min([i for i in arr if i % 2 == 0])
        if smallest is None:
            return result
        for i, num in enumerate(arr):
            if num == smallest:
                result.append([smallest, i])
        return min(result, key=lambda x: x[1])

R:

    def pluck(arr):
        if not arr:
            return []
        even_nums = [x for x in arr if x % 2 == 0]
        if not even_nums:
            return []
        return min(
            enumerate(even_nums),
            key=lambda x: x[1]
        )

