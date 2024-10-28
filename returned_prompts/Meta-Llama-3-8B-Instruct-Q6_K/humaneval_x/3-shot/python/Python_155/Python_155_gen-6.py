    num_str = str(abs(num))
    even_count = sum(1 for c in num_str if int(c) % 2 == 0)
    odd_count = len(num_str) - even_count
    return (even_count, odd_count)  # return a tuple with even and odd counts


