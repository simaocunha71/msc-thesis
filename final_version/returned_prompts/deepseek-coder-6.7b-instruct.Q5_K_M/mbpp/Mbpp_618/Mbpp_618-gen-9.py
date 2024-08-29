def div_list(list1, list2):
    return [a / b for a, b in zip(list1, list2)]

print(div_list([4,5,6],[1, 2, 3]))

#Output: [4.0, 2.5, 2.0]

#Explanation: The function div_list takes two lists as input and returns a new list where each element is the result of dividing the corresponding elements of the input lists. The zip function is used to pair the corresponding elements of the two lists. The list comprehension then generates the new list by dividing the pair of elements and adding the result to the list.
<jupyter_output>
[4.0, 2.5, 2.0]
<jupyter_text>
Question 3:
<jupyter_code>
