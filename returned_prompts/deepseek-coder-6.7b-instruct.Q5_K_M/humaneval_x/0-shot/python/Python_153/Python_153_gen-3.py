
    def Strongest_Extension(class_name, extensions):
        strongest_extension = extensions[0]
        highest_strength = sum([1 for c in extensions[0] if c.isupper()]) - sum([1 for c in extensions[0] if c.islower()])

        for extension in extensions[1:]:
            strength = sum([1 for c in extension if c.isupper()]) - sum([1 for c in extension if c.islower()])
            if strength > highest_strength:
                strongest_extension = extension
                highest_strength = strength

        return f"{class_name}.{strongest_extension}"


print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))

# Output:
# my_class.AA
# Slices.SErviNGSliCes
<jupyter_output>
<empty_output>
<jupyter_text>
Task 3
<jupyter_code>
