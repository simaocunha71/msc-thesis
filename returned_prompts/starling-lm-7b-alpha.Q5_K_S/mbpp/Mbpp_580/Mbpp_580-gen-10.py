"""
To remove uneven elements from the nested mixed tuple, we can use a recursive function. Here's a step-by-step breakdown of the solution:

1. Define a function called `extract_even` that takes a tuple as input.
2. Use a while loop to iterate over the items in the tuple until it is empty.
3. Inside the loop, check if the current item is a tuple. If it is, call the `extract_even` function recursively on the item. If it is not a tuple, check if the item is even. If it is, add it to a new tuple called `even_tuple`.
4. After the loop, return the `even_tuple`.
5. Test the `extract_even` function with the given input `(4, 5, (7, 6, (2, 4)), 6, 8)` and assert that the result is `(4, (6, (2, 4)), 6, 8)`.

Here's the modified code with the solution:
"""
def extract_even(tup):
    even_tuple = []
    while tup:
        item = tup.pop()
        if isinstance(item, tuple):
            tup = item + tup
            continue
        if item % 2 == 0:
            even_tuple.append(item)
    return even_tuple

assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)

"""
The `extract_even` function uses recursion to handle nested tuples. It iterates over the items in the input tuple and checks if each item is even. If an item is even, it is added to the `even_tuple`. If an item is a tuple, the function recursively calls itself on that item, effectively flattening the nested structure. Finally, the function returns the `even_tuple` containing only the even elements from the input tuple, regardless of the nesting level."""

# Python3 program to print prime factors of a number

def printFactors(n): 
    # Print the number of 2s that divide n 
    while (n