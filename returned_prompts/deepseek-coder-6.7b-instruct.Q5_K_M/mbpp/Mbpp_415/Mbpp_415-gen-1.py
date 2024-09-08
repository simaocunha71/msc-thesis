
def max_Product(lst):
    lst.sort()
    if lst[0]*lst[1] > lst[-1]*lst[-2]:
        return (lst[0], lst[1])
    else:
        return (lst[-1], lst[-2])

assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
assert max_Product([-10,-20,1,2,3,4,7,8]) == (-10, -20)
assert max_Product([10,20,30,40,70,0,80,40]) == (70, 80)
assert max_Product([1,2,3,4,7,0,8,4,100]) == (100, 80)
assert max_Product([10,20,0,40,0,40,70,0,80,40]) == (80, 70)

In the given question, we are asked to find a pair with the highest product. Here we are considering the highest product as the product of the two numbers which will give us the highest product irrespective of their positions. 

The sorting of the list is done to bring the highest and lowest numbers to the first and last positions respectively. 

Then we are comparing the product of the first two and last two elements in the list. If the product of the first two elements is greater than the product of the last two elements, we return a tuple with the first two elements. Otherwise, we return a tuple with the last two elements.
"""


"""


