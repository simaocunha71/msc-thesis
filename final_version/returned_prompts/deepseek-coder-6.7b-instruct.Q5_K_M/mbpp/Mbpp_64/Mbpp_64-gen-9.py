def subject_marks(lst):
    return sorted(lst, key=lambda x: x[1])


print(subject_marks([('English', 88),  ('Science', 90),  ('Maths', 97),  ('Social sciences', 82)]))

#  Output: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

"""
Explanation:
In the function, we use the built-in function sorted(). The key argument of the sorted() function is a function that takes a single argument and returns a key to be used for sorting purposes. Here, we use a lambda function that returns the second element of each tuple to sort based on the second element.
"""
<jupyter_output>
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
<jupyter_text>
Question 3
<jupyter_code>
