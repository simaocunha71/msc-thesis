
import re

def Strongest_Extension(class_name, extensions):
    strengths = []
    for ext in extensions:
        strength = re.findall(r'[A-Z]', ext)
        strengths.append(len(strength) - len(re.findall(r'[a-z]', ext)))
    strongest = strengths.index(max(strengths))
    return class_name + '.' + extensions[strongest]

print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC', 'BE', 'cc']))