
    def Strongest_Extension(class_name, extensions):
        strongest_strength = -float('inf')
        strongest_extension = ''

        for extension in extensions:
            cap = sum(1 for c in extension if c.isupper())
            sm = sum(1 for c in extension if c.islower())
            strength = cap - sm

            if strength > strongest_strength:
                strongest_strength = strength
                strongest_extension = extension

        return f'{class_name}.{strongest_extension}'

    print(Strongest_Extension('my_class',  ['AA',  'Be',  'CC']))  # Output: 'my_class.AA'
    print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))  # Output: 'Slices.SErviNGSliCes'

This program loops over each extension in the given list, calculates its strength by subtracting the number of lowercase letters from the number of uppercase letters, then checks if it's the strongest so far. If it is, it updates the strongest strength and extension. Finally, it returns the class name and the strongest extension.
"""


def Strongest_Extension(class_name, extensions):
    strengths = [sum(1 for c in ext if c.isupper()) - sum(1 for c in ext if c.islower()) for ext in extensions]
    strongest_idx = strengths.index(max(strengths))
    return f'{class_name}.{extensions[strongest_idx]}'


print(Strongest_Extension('my_class',  ['AA', 'Be', 'CC']))  # Output: 'my_class.AA'
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))  # Output: 'Slices.SErviNGSliCes'
<jupyter_output>
my_class.AA
Slices.SErviNGSliCes
<jupyter_text>
**Question 6**
<j