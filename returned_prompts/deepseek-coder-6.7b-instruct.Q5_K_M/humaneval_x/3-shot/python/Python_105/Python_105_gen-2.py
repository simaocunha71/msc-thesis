    num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    return [num2words[i] for i in sorted(arr, reverse=True) if 1 <= i <= 9]

