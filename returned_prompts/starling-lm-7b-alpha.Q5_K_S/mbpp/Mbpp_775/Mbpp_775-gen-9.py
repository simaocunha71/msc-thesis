"""
def odd_position(list):
    for i in range(0,len(list),2):
        if list[i] % 2 != 0:
            return False
    return True
"""

def odd_position(list):
    return all(i % 2 != 0 for i in list[::2])

print(odd_position([2,1,4,3,6,7,6,3]))


"""
Explanation:
The function odd_position(list) uses Python’s built-in all() function to check if all elements in a given iterator are true. If any of the elements are false, all() will return False. In this case, it checks if all odd indexed elements in the given list are odd. If any of these elements are not odd, all() will return False, and odd_position() will return False. Otherwise, odd_position() will return True.
"""



















"""
Explanation:
The function odd_position(list) uses a for loop to iterate over the indices of the given list in steps of 2, checking if each index is odd. It uses the modulo operator (%) to check if the element at each odd index is odd. If any of the elements at odd indices are not odd, the function will return False. Otherwise, it will return True.
"""




















"""
Explanation:
The function odd_position(list) uses list comprehension to create a new list containing only the elements at odd indices of the given list. It then uses a for loop to iterate over this new list and checks if each element is odd using the modulo operator (%) and the not operator (!=). If any of the elements are not odd, the function will return False. Otherwise, it will return True.
"""


















"""
Explanation:
The function odd_position(list) uses a generator expression to create a generator that yields only the elements at odd indices of the given list. It then uses the built-in all() function to check if all elements yielded by the generator are odd.