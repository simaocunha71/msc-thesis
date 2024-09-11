def first_second(t):
    return (sum(t),max(t))

# Assert
assert first_second(('Mers', 'for', 'Vers') ) == (12, 'M')




"""
Given a tuple, return a new tuple with the first element being the product of all elements in the tuple, and the second element being the minimum of all elements in the tuple.
assert product_min(('Mers', 'for', 'Vers') ) == (0.0004, 'f')