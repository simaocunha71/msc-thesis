    def by_length(arr: List[int]) -> List[str]:
        names = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        result = []
        for elem in arr:
            if 1 <= elem <= 9:
                result.append(names[elem])
        return result[::-1]


