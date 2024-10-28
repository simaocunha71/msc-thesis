
def words_string(s):
    return s.replace(',', '').split()

print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))
<jupyter_output>
['Hi', 'my', 'name', 'is', 'John']
['One', 'two', 'three', 'four', 'five', 'six']
<jupyter_text>
Exercise 2: Create a function that returns the sum of all the multiples of 3 and 5 between 0 and a given number.
<jupyter_code>
