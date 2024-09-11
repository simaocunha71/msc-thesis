def move_zero(l):
    zeroes = []
    for i in l:
        if i != 0:
            yield i
        else:
            zeroes.append(i)
    for j in zeroes:
        yield j

move_zero([1,0,2,0,3,4])







"""
Explanation:
The function move_zero takes a list as an argument and returns a generator object. It uses a for loop to iterate through the list.
For each element in the list, it checks if the element is not equal to 0.
If the element is not equal to 0, it yields the element.
If the element is equal to 0, it appends the element to the zeroes list.
After the for loop, it uses a for loop to iterate through the zeroes list and yields each element.
Finally, the function returns the generator object.
The assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0] checks if the function correctly moves all the zeroes to the end of the list by comparing the result of the function with the expected result [1,2,3,4,0,0].
"""

"""
Explanation:
The function move_zero takes a list as an argument and returns a generator object. It uses a for loop to iterate through the list.
For each element in the list, it checks if the element is not equal to 0.
If the element is not equal to 0, it yields the element.
If the element is equal to 0, it appends the element to the zeroes list.
After the for loop, it uses a for loop to iterate through the zeroes list and yields each element.
Finally, the function returns the generator object.
The assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0] checks if the function correctly moves all the zeroes to the end of the list by comparing the result of the function with the expected result [1,2,3,4,0,0].
"""

"""
Explanation:
The function move_zero takes a list as an argument and