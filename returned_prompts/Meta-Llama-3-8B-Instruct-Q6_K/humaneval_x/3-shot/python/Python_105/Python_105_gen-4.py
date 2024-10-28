    def digit_name(n):
        if n < 1 or n > 9:
            return ""
        names = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return names[n]

    if not arr:
        return []

    arr = sorted([n for n in arr if 1 <= n <= 9])
    arr = arr[::-1]
    return [digit_name(n) for n in arr]


