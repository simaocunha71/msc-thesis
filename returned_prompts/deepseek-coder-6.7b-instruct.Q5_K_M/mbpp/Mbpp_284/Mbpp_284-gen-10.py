def check_element(lst,element):
    return all(el == element for el in lst)

print(check_element(["green", "orange", "black", "white"],'blue'))

# The function 'check_element' takes in a list and an element. It uses the built-in function 'all()' which returns True if all items in an iterable (in this case list) are True. The function 'all()' stops and returns False as soon as it encounters an item that is False, making it more efficient than a for loop. Inside the parentheses of 'all()', we use a generator comprehension to check if all items in the list are equal to the given element. If they are, the function returns True; otherwise it returns False.
<jupyter_output>
False
<jupyter_text>
Exercise 2
<jupyter_code>
