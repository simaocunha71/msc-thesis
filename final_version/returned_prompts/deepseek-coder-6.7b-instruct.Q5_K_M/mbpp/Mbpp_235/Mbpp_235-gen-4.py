def even_bit_set_number(n):
    bin_n = bin(n)[2:]
    bin_n = list(bin_n)
    for i in range(len(bin_n)):
        if i % 2 == 0:
            bin_n[i] = '1'
    bin_n = "".join(bin_n)
    return int(bin_n, 2)

print(even_bit_set_number(10))
assert even_bit_set_number(10) == 10


