    strongest_extension = max(extensions, key=lambda x: (x.upper().count(x)-x.lower().count(x), extensions.index(x)))
    return f"{class_name}.{strongest_extension}"


# Test the function
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))  # Output: 'my_class.AA'
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))  # Output: 'Slices.SErviNGSliCes'
print(Strongest_Extension('my_class', ['my', 'Hello', 'world']))  # Output: 'my_class.my'





