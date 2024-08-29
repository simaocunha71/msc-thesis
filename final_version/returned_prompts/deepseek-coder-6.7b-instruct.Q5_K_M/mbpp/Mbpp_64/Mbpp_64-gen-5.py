def subject_marks(lst):
    return sorted(lst, key = lambda x: x[1])

print(subject_marks([('English', 88),  ('Science', 90),  ('Maths', 97),  ('Social sciences', 82)]))

# Output: [('Social sciences', 82),  ('English', 88),  ('Science', 90),  ('Maths', 97)]

# Here we are using the sorted function with the key parameter as a lambda function that returns the second element of each tuple.
# The sorted function sorts the list of tuples based on the key.
<jupyter_output>
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
<jupyter_text>
