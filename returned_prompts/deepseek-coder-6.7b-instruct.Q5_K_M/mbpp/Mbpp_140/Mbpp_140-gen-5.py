
def extract_singly(list_of_tuples):
    result = []
    for tup in list_of_tuples:
        result.extend(tup)
    return set(result)

print(set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])))
<jupyter_output>
{1, 3, 4, 5, 7}
<jupyter_text>
Q6. Write a function that takes a list of numbers and returns the sum of squares of all even numbers in the list.
<jupyter_code>
