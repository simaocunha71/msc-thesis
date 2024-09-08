def check_element(lst, elm):
    return all(el == elm for el in lst)

print(check_element(["green",  "white"],'white'))

#Output: True

print(check_element(["green", "orange", "black", "white"],'blue'))

#Output: False

# Explanation: In the first case, all elements in the list are 'white' so it returns True. In the second case, not all elements are 'blue' so it returns False.

