
def Strongest_Extension(class_name, extensions):
    strength = 0
    strongest_extension = ''
    for ext in extensions:
        cap = 0
        sm = 0
        for char in ext:
            if char.isupper():
                cap += 1
            elif char.islower():
                sm += 1
        strength_ext = cap - sm
        if strength_ext > strength:
            strength = strength_ext
            strongest_extension = ext
    return "{}.{}".format(class_name, strongest_extension)

# Tests
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))  # 'my_class.AA'
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))  # 'Slices.SErviNGSliCes'
print(Strongest_Extension('Another_class', ['AA', 'be', 'cc']))  # 'Another_class.AA'
print(Strongest_Extension('Another_class', ['AA', 'bb', 'cc']))  # 'Another_class.AA'

# Answer:

def Strongest_Extension(class_name, extensions):
    strength = 0
    strongest_extension = ''
    for ext in extensions:
        cap = 0
        sm = 0
        for char in ext:
            if char.isupper():
                cap += 1
            elif char.islower():
                sm += 1
        strength_ext = cap - sm
        if strength_ext > strength:
            strength = strength_ext
            strongest_extension = ext
    return "{}.{}".format(class_name, strongest_extension)

# Tests
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))  # 'my_class.AA'
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))  # 'Slices.SErviNGSliCes'
print(Strongest_Extension('An