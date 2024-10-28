```
def unique_product(lst):
    unique_nums = list(set(lst))
    product = 1
    for num in unique_nums:
        product *= num
    return product
```
This function first converts the list to a set, which automatically removes any duplicate numbers. It then initializes a product variable to 1 and iterates over the unique numbers, multiplying the product by each number. The function finally returns the product. 

The unit test `assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000` ensures that the function works correctly, as the product of the unique numbers in the list is indeed 720000000. 

Please note that this function does not preserve the original order of the numbers in the list. If you need to preserve the order, you can convert the list to a set and then convert it back to a list. However, this would still remove any duplicate numbers, not necessarily in the same order they appeared in the original list. If you need to preserve the order of the numbers and also remove duplicates, you would need to use a different approach. 

For example, you could use a dictionary to keep track of the count of each number in the list, and then multiply the numbers together based on their count. This would also work correctly even if the list contains duplicate numbers. Here is an example of how you could implement this:

```
def unique_product(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    product = 1
    for num, count in count_dict.items():
        product *= num ** count
    return product
```

This function works by first creating a dictionary where the keys are the unique numbers in the list and the values are the counts of each number. It then initializes a product variable to 1 and iterates over the dictionary, multiplying the product by each number raised to the power of its count. The function finally returns the product. This function preserves the order of the numbers in the list and also removes duplicates. However, it does not preserve the original order of the numbers in the list. If you need to preserve the original order, you would need to use a different approach. 

For example, you could use a list comprehension to create a new list that contains each number in the original list as