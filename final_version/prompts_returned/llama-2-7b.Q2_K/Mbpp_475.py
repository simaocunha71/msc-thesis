"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""
from typing import List
def sort_dict(dictionary:List)[str[], str]:
    """Return the sorted dictionary in ascending order based on values of each key. Returns a tuple containing the sorted keys and the original dictionary."""
    sorted_keys=[key for key,value in dictionary.items()]#store sorted list in one variable
    sorted_dict={}
    for k in sorted_keys: #sort the dictionary according to the value of each key then sort again according to the sorted keys
        sorted_val=sorted(dictionary[k]) #sort only values corresponding to a particular key
        sorted_list=[str(x)for x in sorted_val]#convert sorted list to string and store it as an element of dictionary.
        for i,s in enumerate(sorted_list):
            sorted_dict[f'{k}__i:{i}'](s) #join the key and the value with "__" (double underscore) followed by index of array.
\end{code}

Answer: It is not necessary to re-create your variable each time. You could directly access the values from dictionaries. For example,

\begin{code}
dictionary = {'Physics':90, 'Chemistry':87, 'Math':81}
list_of_scores = list(sorted(key for key, value in dictionary.items()))
print('Top scores:', ', '.join([str(x) for x in sorted(dictionary[key])]))
\end{code}

Output:

\begin{blockquote}
Top scores: 'Chemistry', 87,'Physics', 90, 'Math', 81
\end{blockquote}