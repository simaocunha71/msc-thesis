def multiply_elements(tup):
    return tuple(tup[i]*tup[i+1] for i in range(len(tup)-1))

print(multiply_elements((1, 5, 7, 8, 10)))  # (5, 35, 56, 80)

# ---------

