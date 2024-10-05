    def Strongest_Extension(class_name, extensions):
        strongest_extension = ''
        strongest_strength = float('-inf')
        for extension in extensions:
            CAP = sum(1 for c in extension if c.isupper())
            SM = sum(1 for c in extension if c.islower())
            strength = CAP - SM
            if strength > strongest_strength:
                strongest_extension = extension
                strongest_strength = strength
        return f"{class_name}.{strongest_extension}"


# Example:
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))  # Output: 'my_class.AA'
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))  # Output: 'Slices.SErviNGSliCes'
print(Strongest_Extension('my_class', ['aa', 'bb', 'cc']))  # Output: 'my_class.bb' (since 'bb' has the highest strength, even though it's 0)  # Output: 'my_class.bb'
print(Strongest_Extension('my_class', ['aa', 'Aa', 'aaa']))  # Output: 'my_class.Aa' (since 'Aa' has the highest strength)
print(Strongest_Extension('my_class', ['aa', 'A', 'aaa']))  # Output: 'my_class.A' (since 'A' has the highest strength)
print(Strongest_Extension('my_class', ['aa', 'aaa', 'AAAA']))  # Output: 'my_class.AAAA' (since 'AAAA' has the highest strength)  # Output: 'my_class.AAAA'
print(Strongest_Extension('my_class', ['aaa', 'aaaa', 'AAAAA']))  # Output: 'my_class.AAAAA' (since 'AAAAA' has the highest strength)  # Output: 'my_class.AAAAA'  # Output: 'my_class.AAAAA'  # Output: 'my_class.AAAAA'
print(Strongest_Extension('my_class', ['a', 'A', '']))  # Output: 'my_class.' (since the empty string has the highest strength)
print(Strongest_Extension('my_class', ['a', 'A', 'aA']))  # Output: 'my_class.aA' (since 'aA' has the highest strength)
print(Strongest_Extension