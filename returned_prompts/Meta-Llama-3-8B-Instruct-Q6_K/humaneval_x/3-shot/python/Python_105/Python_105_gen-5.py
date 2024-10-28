    def digit_names(n):
        return {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
        }.get(n, "Invalid number")

    result = []
    for num in sorted([n for n in arr if 1 <= n <= 9]):
        result.append(digit_names(num))
    return result[::-1] if arr else []
    # return [digit_names(num) for num in sorted([n for n in arr if 1 <= n <= 9])[::-1]] if arr else []  # Alternate solution
    # return [digit_names(num) for num in sorted([n for n in arr if isinstance(n, int) and 1 <= n <= 9])[::-1]] if arr else []  # Alternate solution


