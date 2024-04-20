"""
Write a python function to find the product of the array multiplication modulo n.
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""

def find_remainder(arr,n):
    product=1; remainder=0
    for i in arr:
        product = product*(i) % n
        print("product is",product,"modulo of ",n,"is",product%n,"and the remaining digit is" ) #to get the remianing digit we have to find the modulo of product.
\end{code}