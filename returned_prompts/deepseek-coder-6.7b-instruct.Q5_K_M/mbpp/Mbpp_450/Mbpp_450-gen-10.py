def extract_string(lst,n):
    return [i for i in lst if type(i)==str and len(i)>n]

print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'],8))

#Output: ['practice', 'solution']

#Explanation: The function extract_string will go through each element in the list and if it's a string that has a length greater than n, it will append it to the resultant list. It will return this list.
#The condition type(i)==str checks if the element is a string. The condition len(i)>n checks if the length of the string is greater than n.

#Note: The condition len(i)>=n would return all strings of length equal to and greater than n.
<jupyter_output>
['practice', 'solution']
<jupyter_text>
Question 10:
<jupyter_code>
