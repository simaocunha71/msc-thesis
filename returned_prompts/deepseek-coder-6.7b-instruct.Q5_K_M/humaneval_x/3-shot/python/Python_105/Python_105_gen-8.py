    num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    one_to_nine = [x for x in arr if 1 <= x <= 9]
    one_to_nine.sort(reverse=True)
    return [num2words[x] for x in one_to_nine]


