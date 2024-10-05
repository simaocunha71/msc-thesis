    def tri(n):
        if n == 0:
            return []
        elif n == 1:
            return [1]
        elif n == 2:
            return [1, 3]
        else:
            result = [1, 3]
            while len(result) < n + 1:
                if len(result) % 2 == 0:
                    result.append(1 + result[len(result) - 1] / 2)
                else:
                    result.append(result[len(result) - 1] + result[len(result) - 2] + result[len(result) - 3])
            return result


