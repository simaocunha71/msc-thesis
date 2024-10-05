    def by_length(arr):
        sorted_arr = sorted(arr, key=lambda x: x if 1 <= x <= 9 else float('inf'))[::-1]
        result = []
        for elem in sorted_arr:
            if 1 <= elem <= 9:
                result.append(str(elem))
        return result

    def by_length(arr):
        result = []
        for elem in arr:
            if elem >= 1 and elem <= 9:
                result.append(str(elem))
        return result

    def by_length(arr):
        result = []
        for elem in arr:
            if elem >= 1 and elem <= 9:
                result.append(str(elem))
        result.sort(key=lambda x: x)
        return result[::-1]

    def by_length(arr):
        result = []
        for elem in arr:
            if elem >= 1 and elem <= 9:
                result.append(str(elem))
        result.sort(key=lambda x: x)
        result = result[::-1]
        return result

    def by_length(arr):
        result = []
        for elem in arr:
            if elem >= 1 and elem <= 9:
                result.append(str(elem))
        result.sort(key=lambda x: x, reverse=True)
        return result

    def by_length(arr):
        result = []
        for elem in arr:
            if elem >= 1 and elem <= 9:
                result.append(str(elem))
        result.sort(key=lambda x: x)
        return result

    def by_length(arr):
        result = []
        for elem in arr:
            if elem >= 1 and elem <= 9:
                result.append(str(elem))
        result.sort(reverse=True)
        return result

    def by_length(arr):
        result = []
        for elem in arr:
            if elem >= 1 and elem <= 9:
                result.append(str(elem))
        result