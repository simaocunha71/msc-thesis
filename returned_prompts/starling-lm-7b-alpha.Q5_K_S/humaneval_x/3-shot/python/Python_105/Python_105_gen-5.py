    def by_length(arr):
        name = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        result = []
        for elem in arr:
            if 1 <= elem <= 9:
                result.append(name[elem - 1])
        return result


