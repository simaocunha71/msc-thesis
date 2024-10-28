    def sort_even(l: List[int]) -> List[int]:
        result = []
        for idx, elem in enumerate(l):
            if idx % 2 == 0:
                result.append(elem)
        result.extend(sorted(elem for idx, elem in enumerate(l) if idx % 2 == 1))
        return result


