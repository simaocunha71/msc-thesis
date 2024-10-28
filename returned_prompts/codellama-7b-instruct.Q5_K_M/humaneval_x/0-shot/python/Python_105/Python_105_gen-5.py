
    import re
    
    def by_length(arr):
        arr = sorted(arr)
        arr = list(map(lambda x: str(x), arr))
        arr = [re.sub('1', 'One', x) for x in arr]
        arr = [re.sub('2', 'Two', x) for x in arr]
        arr = [re.sub('3', 'Three', x) for x in arr]
        arr = [re.sub('4', 'Four', x) for x in arr]
        arr = [re.sub('5', 'Five', x) for x in arr]
        arr = [re.sub('6', 'Six', x) for x in arr]
        arr = [re.sub('7', 'Seven', x) for x in arr]
        arr = [re.sub('8', 'Eight', x) for x in arr]
        arr = [re.sub('9', 'Nine', x) for x in arr]
        arr = list(map(lambda x: x[::-1], arr))
        return arr

    # Tests
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    assert by_length([]) == []
    assert by_length([1, -1 , 55]) == ['One']
