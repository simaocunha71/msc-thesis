def Strongest_Extension(class_name, extensions):
    strongest_extension = max(extensions, key=lambda x: sum(1 for c in x if c.isupper) - sum(1 for c in x if c.islower))
    return f"{class_name}.{strongest_extension}"

print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))  # Output: my_class.AA
print(Strongest_Extension('person', ['A', 'B', 'a']))  # Output: person.A
print(Strongest_Extension('animal', ['A', 'a', 'B']))  # Output: animal.A
print(Strongest_Extension('car', ['c', 'A', 'b']))  # Output: car.A
print(Strongest_Extension('student', ['Stu', 'd', 'ent']))  # Output: student.Stu
print(Strongest_Extension('student', ['stu', 'd', 'ent']))  # Output: student.stu
print(Strongest_Extension('student', ['stu', 'ent', 'd']))  # Output: student.stu
print(Strongest_Extension('student', ['stu', 'ent', 'D']))  # Output: student.stu
print(Strongest_Extension('student', ['stu', 'ent', 'd', 'D']))  # Output: student.stu
print(Strongest_Extension('student', ['stu', 'ent', 'd', 'D', 'A']))  # Output: student.stu
print(Strongest_Extension('student', ['stu', 'ent', 'd', 'D', 'a']))  # Output: student.stu
print(Strongest_Extension('student', ['stu', 'ent', 'd', 'D', 'a', 'A']))  # Output: student.stu
print(Strongest_Extension('student', ['stu', 'ent', 'd', 'D', 'a', 'A', 'b']))  # Output: student.stu
print(Strongest_Extension('student', ['stu', 'ent', 'd', 'D', 'a', 'A', 'b', 'c']))  # Output: student.stu
print(Strongest_Extension('student',