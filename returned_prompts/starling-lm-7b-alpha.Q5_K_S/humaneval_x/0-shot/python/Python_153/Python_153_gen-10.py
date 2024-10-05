
def Strongest_Extension(class_name, extensions):
    CAP = sum([c.isupper() for c in extensions[0]])
    SM = sum([c.islower() for c in extensions[0]])
    strength = CAP - SM
    strongest_extension = extensions[0]
    for ext in extensions[1:]:
        CAP = sum([c.isupper() for c in ext])
        SM = sum([c.islower() for c in ext])
        if CAP - SM == strength:
            strongest_extension = ext
        elif CAP - SM > strength:
            strength = CAP - SM
            strongest_extension = ext
    return class_name + '.' + strongest_extension

# def Strongest_Extension(class_name, extensions):
#     strengths = [sum([c.islower() for c in ext]) - sum([c.isupper() for c in ext]) for ext in extensions]
#     strongest_index = strengths.index(max(strengths))
#     return class_name + '.' + extensions[strongest_index]



# for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))


# for Strongest_Extension('my_class', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'my_class.SErviNGSliCes'
print(Strongest_Extension('my_class', ['SErviNGSliCes', 'Cheese', 'StuFfed']))


# for Strongest_Extension('my_class', ['abc', 'def', 'ghi']) == 'my_class.abc'
print(Strongest_Extension('my_class', ['abc', 'def', 'ghi']))


# for Strongest_Extension('my_class', ['aa', 'bb', 'cc']) == 'my_class.aa'
print(Strongest_Extension('my_class', ['aa', 'bb', 'cc']))


# for Strongest_Extension('my_class', ['CC