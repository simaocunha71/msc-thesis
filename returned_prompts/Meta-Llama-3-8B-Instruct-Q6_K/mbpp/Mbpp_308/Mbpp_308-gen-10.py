```
def large_product(list1, list2, n):
    if n > len(list1) * len(list2):
        return "Error: n is larger than the total number of combinations"
    products = [(a, b) for a in list1 for b in list2]
    products.sort(key=lambda x: x[0]*x[1], reverse=True)
    return [x[0]*x[1] for x in products[:n]]
```
The function `large_product` takes two lists of numbers and an integer `n` as inputs. It calculates all possible products of one number from each list, sorts them in descending order, and returns the `n` largest products.

The unit test `assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]` ensures that the function works correctly. It tests the function with two lists of numbers and `n=3`, and checks if the returned result is as expected. If the function works correctly, it should return the list `[60, 54, 50]`. If the function returns anything else, the test will fail, indicating that the function is not working correctly. 

The function first generates all possible products by using list comprehension. It then sorts these products in descending order based on their values. Finally, it returns the `n` largest products by slicing the sorted list. If `n` is larger than the total number of combinations, the function returns an error message. 

The time complexity of this function is O(n*m*log(n*m)), where n and m are the lengths of the input lists. The space complexity is O(n*m), as the function needs to store all possible products in memory. 