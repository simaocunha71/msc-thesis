def Strongest_Extension(class_name, extensions):
    def extension_strength(extension):
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        return cap - sm

    strongest_extension = max(extensions, key=extension_strength)
    return f"{class_name}.{strongest_extension}"
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC'])) # 'my_class.AA' 
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])) # 'Slices.SErviNGSliCes'
print(Strongest_Extension('my_class', ['a', 'B', 'c'])) # 'my_class.B' 
print(Strongest_Extension('my_class', ['A', 'b', 'c'])) # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'  # 'my_class.A'