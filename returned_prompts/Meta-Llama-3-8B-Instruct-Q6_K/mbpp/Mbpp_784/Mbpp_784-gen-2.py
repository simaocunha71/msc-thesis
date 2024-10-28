```
def mul_even_odd(lst):
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    if even and odd:
        return even[0] * odd[0]
    else:
        return 0
```    
The function takes a list as input, and returns the product of the first even and odd number in the list. If the list does not contain both even and odd numbers, it returns 0.

The unit test `assert mul_even_odd([1,3,5,7,4,1,6,8])==4` helps to clarify the problem. It suggests that the function should return the product of the first even and odd numbers in the list, and 0 if the list does not contain both even and odd numbers. This is because the product of 4 (the first even number in the list) and 1 (the first odd number in the list) is 4, which matches the expected output.

The function uses list comprehensions to create two lists, one for even numbers and one for odd numbers. It then checks if both lists are not empty, and if so, returns the product of the first elements of the lists. If either list is empty, it returns 0.