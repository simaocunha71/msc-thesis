    def num_to_name(n):
        num_dict = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
            7: "Seven", 8: "Eight", 9: "Nine"
        }
        return num_dict.get(n, "Invalid number")

    result = [num_to_name(i) for i in sorted([i for i in arr if 1 <= i <= 9])]
    result.reverse()
    return result
    # or return [num_to_name(i) for i in sorted([i for i in arr if 1 <= i <= 9])[::-1]] if you prefer the reverse function


