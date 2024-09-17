```
def unique_product(lst):
    unique_nums = set(lst)
    product = 1
    for num in unique_nums:
        product *= num
    return product
```
Explanation:
The function `unique_product` takes a list of numbers as input and returns the product of the unique numbers in the list. It does this by converting the list to a set, which removes any duplicate numbers, and then multiplying the remaining numbers together. The unit test `assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000` checks that the function returns the correct product for a given list. This test is important because it ensures that the function works correctly when there are duplicate numbers in the list. Without this test, we would not know whether the function is working correctly. 

The time complexity of this function is O(n), where n is the number of unique numbers in the list. This is because we are iterating over the unique numbers once to calculate their product. The space complexity is also O(n), because we are storing the unique numbers in a set. 

Note that this function assumes that the input list contains only numbers. If the list can contain non-numeric values, the function would need to be modified to handle this case. For example, we could add a check to see if each element in the list is a number before trying to multiply it with the product. This would add to the complexity of the function, but would ensure that it works correctly for all possible inputs. 