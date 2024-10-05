
    def count_upper(extension):
        return sum(1 for c in extension if c.isupper())

    def count_lower(extension):
        return sum(1 for c in extension if c.islower())

    def strength(extension):
        return count_upper(extension) - count_lower(extension)

    extensions.sort(key=strength, reverse=True)

    return f"{class_name}.{extensions[0]}"

print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))
print(Strongest_Extension('Class', ['aAa', 'bbB', 'CCc', 'ddD']))
print(Strongest_Extension('Class', ['Aa', 'BB', 'cc', 'DD']))
<jupyter_output>
Slices.SErviNGSliCes
my_class.AA
Class.ddD
Class.BB
<jupyter_text>
Problem 3. Calculate the sum of the digits of the factorial of a number
<jupyter_code>
