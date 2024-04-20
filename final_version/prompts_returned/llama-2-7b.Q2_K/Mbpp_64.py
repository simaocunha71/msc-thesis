"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
import math

def subject_marks(subjects):
    marks=[] #make an empty list to store the sorted subjcets

    for x in subjects: #(loop through each element of a list)
        if type(x[1])==int: #(check what type of data is the 2nd element of tuple in subject_marks function)
            marks.append((x[0],float(math.log10(abs(x[1]))))) #if its an int,then just put it into a sorted list with the data from the second element
        else: #(else add elements which are not ints to list)
            if type(x[1])==str:
                marks.append((x[0],float(abs(x[1]-48)) )) #change the log10 to abs() to avoid a division by zero error
    return marks
    
subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])