def sample_nam(names):
    return sum(len(name) for name in names if name[0].isupper())

print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))

#The function works by iterating over each name in the list. If the name starts with an uppercase letter (checked by isupper() method), it is included in the sum. The sum of the lengths of these names is returned.

#The sum function adds up all the lengths of the names, and the generator expression inside the sum function is used to create each length. This is a bit like a loop that creates the lengths on the fly.

#This will print out 16 because the lengths of 'Dylan', 'Diana', 'Joanne' are 5, 6, and 7 respectively. So, the total is 5+6+7=16.

#Note: This function assumes that the names in the list are all strings. If this isn't the case, the function could potentially throw an error.
<jupyter_output>
16
<jupyter_text>
**Question 2**
<jupyter_code>
