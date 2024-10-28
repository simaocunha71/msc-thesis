

    evens = sorted(l[::2])
    l_prime = l[:]
    l_prime[::2] = evens
    return l_prime


print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))


# 4.

