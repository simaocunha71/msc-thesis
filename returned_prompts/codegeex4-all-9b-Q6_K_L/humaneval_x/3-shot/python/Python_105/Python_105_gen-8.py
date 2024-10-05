    numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [numbers[i - 1] for i in sorted(arr) if 1 <= i <= 9][::-1]