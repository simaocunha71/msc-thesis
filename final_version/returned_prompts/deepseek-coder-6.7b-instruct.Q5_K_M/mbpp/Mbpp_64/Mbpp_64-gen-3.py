
def subject_marks(lst):
    return sorted(lst, key=lambda x: x[1])

print(subject_marks([('English', 88),  ('Science', 90),  ('Maths', 97),  ('Social sciences', 82)]))
<jupyter_output>
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
<jupyter_text>
