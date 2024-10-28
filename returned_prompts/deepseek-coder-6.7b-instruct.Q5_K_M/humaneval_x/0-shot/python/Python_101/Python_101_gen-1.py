
def words_string(s):
    return s.replace(',', '').split()

print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))

# The function words_string is defined and takes a string s as input.
# The replace function is used to remove all the commas from the string s.
# The split function is used to split the string s into words based on spaces.
# The resulting list of words is returned.
<jupyter_output>
['Hi', 'my', 'name', 'is', 'John']
['One', 'two', 'three', 'four', 'five', 'six']
<jupyter_text>
Exercise 2: Lists and LoopsWrite a Python program that takes a list of integers and returns a new list with the squares of the elements in the original list.
<jupyter_code>
