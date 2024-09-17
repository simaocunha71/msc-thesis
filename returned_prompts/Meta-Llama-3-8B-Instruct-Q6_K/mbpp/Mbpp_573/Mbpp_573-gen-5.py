```
def unique_product(lst):
    unique_nums = list(set(lst))
    product = 1
    for num in unique_nums:
        product *= num
    return product
```


The function takes a list of numbers as an argument. It first converts the list into a set, which removes all duplicates. Then it initializes a variable `product` to 1. It iterates over the unique numbers and multiplies the `product` by each number. Finally, it returns the `product`. This function assumes that the input list is not empty and does not contain zero. If there's a possibility of zero or empty list, you should add error checking code. The unit test provided, `assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000`, suggests that the input list is a list of integers. The function should return the product of the unique integers in the list. The output of this function for the given test case is 720000000, which is the product of the unique integers in the list [10, 20, 30, 40, 50, 60]. The time complexity of this function is O(n), where n is the number of unique elements in the list, because it needs to iterate over the unique numbers. The space complexity is also O(n), because it needs to store the unique numbers in a set. 