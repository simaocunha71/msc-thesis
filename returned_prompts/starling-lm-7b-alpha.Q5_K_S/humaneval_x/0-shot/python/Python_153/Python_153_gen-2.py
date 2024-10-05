
def Strongest_Extension(class_name, extensions):
    # Initialize variables
    strongest_extension = ""
    strongest_strength = -100000000
    # Iterate through the list of extensions
    for extension in extensions:
        # Calculate the strength of the current extension
        strength = sum(c.isupper() for c in extension) - sum(c.islower() for c in extension)
        # Check if the strength of the current extension is stronger than the strongest one found so far
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
    # Return the name of the class and the strongest extension
    return ".".join([class_name, strongest_extension])


# Tests
print(Strongest_Extension("my_class", ['AA', 'Be', 'CC'])) # Should print: my_class.AA
print(Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'])) # Should print: Slices.SErviNGSliCes

# Explanation:
# The function takes the class name and a list of extensions as input. It initializes
# two variables: strongest_extension, which will store the name of the strongest extension,
# and strongest_strength, which will store the strength of the strongest extension found so far.
# It then iterates through the list of extensions. For each extension, it calculates the
# strength of the extension (the number of uppercase letters minus the number of lowercase letters),
# and checks if this strength is stronger than the strongest strength found so far. If it is, it updates
# the strongest_extension and strongest_strength variables. Finally, it returns the name of the class concatenated
# with the name of the strongest extension.
# Note: This solution is not the most efficient one, but it is simple and easy to understand.

































































