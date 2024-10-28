    num = abs(num)
    num_str = str(num)
    even_count = sum(1 for c in num_str if c in '02468')
    odd_count = sum(1 for c in num_str if c in '13579')
    return (even_count, odd_count)

