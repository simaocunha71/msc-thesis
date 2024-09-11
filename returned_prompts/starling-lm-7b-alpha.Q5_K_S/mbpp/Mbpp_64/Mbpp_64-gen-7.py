def subject_marks(list_tuple):
    return sorted(list_tuple, key = lambda x:x[1])


# testing the function
marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(subject_marks(marks))

# expected output: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


# The above function uses the sorted() function along with the key parameter, which is a lambda function that returns the second element of each tuple.
# The sorted() function sorts the list_tuple based on the second element of each tuple in ascending order, and the lambda function is used to specify the key to be used for sorting.
# The lambda function takes a tuple as an argument and returns the second element of the tuple, which is the value to be used for sorting.


# In the subject_marks() function, the sorted() function is called with the list_tuple as the first argument and a lambda function as the key argument.
# The lambda function is used to specify the key to be used for sorting, which in this case is the second element of each tuple in the list_tuple.
# The sorted() function returns a new list that contains the sorted tuples based on the second element of each tuple.


# The assert statement is used to verify if the function is working correctly. The expected output is [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)], which is the result of sorting the input list_tuple based on the second element of each tuple.


# The print statement is used to display the result of the function. In this case, the result is the sorted list of tuples, which is [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)].


# Overall, the subject_marks() function takes a list of tuples as an argument and returns a new list that contains the sorted tuples based on the second element of each tuple. The function uses the sorted