def subject_marks(lst):
    return sorted(lst, key=lambda x: x[1])

print(subject_marks([('English', 88),  ('Science', 90),  ('Maths', 97),  ('Social sciences', 82)]))

#output: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# Explanation:
# The sorted function is used to sort the list. The key parameter is set to a lambda function which returns the second element of each tuple. The default order is ascending, and this is used to sort the tuples by the second element.
<jupyter_output>
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
<jupyter_text>
Question 3:
<jupyter_code>
