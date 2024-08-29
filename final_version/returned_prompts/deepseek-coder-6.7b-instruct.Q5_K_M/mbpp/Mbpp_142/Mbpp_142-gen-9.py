def count_samepair(l1, l2, l3):
    return sum(x == y == z for x, y, z in zip(l1, l2, l3))

print(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]))

This function uses the built-in zip function to create a list of tuples, where each tuple contains the corresponding elements from the three input lists. It then uses the built-in sum function and a generator to count the number of tuples where all elements are equal.
"""

