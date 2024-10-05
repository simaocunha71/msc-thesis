    def num_to_name(n):
        names = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return names[n] if 0 <= n <= 9 else ""

    result = [num_to_name(n) for n in sorted([n for n in arr if 1 <= n <= 9], reverse=True)]
    return result
    # Alternative solution
    result = [num_to_name(n) for n in sorted([n for n in arr if 1 <= n <= 9], reverse=True)]
    return result


