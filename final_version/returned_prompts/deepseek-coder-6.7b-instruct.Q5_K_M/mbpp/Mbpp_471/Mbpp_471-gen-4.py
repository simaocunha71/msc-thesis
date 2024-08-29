
def find_remainder(arr,n):
    product = 1
    for num in arr:
        product = (product * num) % n
    return product

print(find_remainder([ 100, 10, 5, 25, 35, 14 ],11)) # 9


"""
Explanation:

The function find_remainder accepts an array and a number n. It initializes the variable product to 1.
Then it iterates over the array using a for loop. For each number in the array, it multiplies the current value of product with the number and then takes modulo n of the result. This is done to handle the situation where the product might exceed the limit of the integer in python.
Finally, it returns the value of product.
"""

"""
