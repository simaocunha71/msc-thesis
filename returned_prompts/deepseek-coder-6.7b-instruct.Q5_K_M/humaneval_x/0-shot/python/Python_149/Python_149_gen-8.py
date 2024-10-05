
def sorted_list_sum(lst):
    lst = [i for i in lst if len(i) % 2 == 0]
    lst.sort(key=lambda x: (len(x), x))
    return lst

#Test Cases
print(sorted_list_sum(["aa", "a", "aaa"])) #=> ["aa"]
print(sorted_list_sum(["ab", "a", "aaa", "cd"])) #=> ["ab", "cd"]

# The function takes a list of strings as input. 
# It removes the strings of odd lengths using a list comprehension that checks if the length of the string is even.
# It sorts the list first by length of the strings, then alphabetically using the sort method with a lambda function that returns a tuple.
# The function returns the sorted list.
<jupyter_output>
['aa']
['ab', 'cd']
<jupyter_text>
Question 4: Write a Python function that accepts a list of integers and returns the count of all even numbers in the list.
<jupyter_code>
