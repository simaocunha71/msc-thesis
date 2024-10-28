
def Strongest_Extension(class_name, extensions):
    strongest_extension = extensions[0]
    strongest_strength = sum([1 for c in extensions[0] if c.isupper()]) - \
                         sum([1 for c in extensions[0] if c.islower()])
    for extension in extensions[1:]:
        strength = sum([1 for c in extension if c.isupper()]) - \
                   sum([1 for c in extension if c.islower()])
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
    return f'{class_name}.{strongest_extension}'

# Test cases
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))  # Output: 'Slices.SErviNGSliCes'
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))  # Output: 'my_class.AA'
print(Strongest_Extension('Pizza', ['pIZZa', 'CheEse', 'tOmAto']))  # Output: 'Pizza.pIZZa'
print(Strongest_Extension('Pasta', ['PaSsAn', 'CheEse', 'CaRBOnA']))  # Output: 'Pasta.CaRBOnA'
<jupyter_output>
Slices.SErviNGSliCes
my_class.AA
Pizza.pIZZa
Pasta.CaRBOnA
<jupyter_text>
Question 2:
<jupyter_code>
