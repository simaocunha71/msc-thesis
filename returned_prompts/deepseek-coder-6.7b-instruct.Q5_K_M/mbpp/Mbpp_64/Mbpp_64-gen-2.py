
def subject_marks(lst):
    return sorted(lst, key=lambda x: x[1])

print(subject_marks([('English', 88),  ('Science', 90),  ('Maths', 97),  ('Social sciences', 82)]))

# Output: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

In this code, we use the built-in sorted() function to sort the list of tuples. The key argument is set to a lambda function that returns the second element of each tuple.
<jupyter_output>
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
<jupyter_text>
