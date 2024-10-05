def Strongest_Extension(class_name, extensions):
    max_cap = -float('inf')
    max_str = ''
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        if cap - sm > max_cap:
            max_cap = cap - sm
            max_str = ext
    return class_name + '.' + max_str

print Strongest_Extension('my_class', ['AA', 'Be', 'CC'])