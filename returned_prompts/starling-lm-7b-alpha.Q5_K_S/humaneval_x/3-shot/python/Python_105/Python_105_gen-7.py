    arr = sorted(list(filter(lambda x: 1 <= x <= 9, arr)), reverse=True)
    arr = list(map(lambda x: ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][x - 1], arr))
    return arr


