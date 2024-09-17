```
def diff_even_odd(lst):
    even = [i for i in lst if i % 2 == 0]
    odd = [i for i in lst if i % 2 != 0]
    if not even or not odd:
        return None
    return even[0] - odd[0]
```    
The function first creates two lists, one for even numbers and one for odd numbers. It then checks if either list is empty. If either list is empty, it returns None. If not, it returns the difference of the first even and first odd numbers. The unit test provided ensures that the function works correctly. For example, the test `assert diff_even_odd([1,3,5,7,4,1,6,8])==3` checks that the function returns the correct difference for the list `[1,3,5,7,4,1,6,8]`.   
   
   In this solution, I used list comprehensions to create the lists of even and odd numbers. I also used the modulus operator (`%`) to check if a number is even or odd. If the remainder of the division of the number by 2 is 0, the number is even; otherwise, it's odd. The function then returns the difference of the first even and first odd numbers. If either list is empty, the function returns None.   
   
   This solution assumes that the input list is not empty and contains at least one even and one odd number. If the list is empty or does not contain at least one even and one odd number, the function may not work as expected. You may want to add additional error checking to handle these cases.   
   
   The time complexity of this solution is O(n), where n is the length of the input list, because it needs to iterate over the list twice to create the lists of even and odd numbers. The space complexity is also O(n), because it needs to store the lists of even and odd numbers.   
   
   You can further improve this solution by using the `min` function to find the smallest even and odd numbers, instead of iterating over the lists. This would reduce the time complexity to O(n) and the space complexity to O(1). However, this would make the solution more complex and harder to understand.   
   
   Here is the improved solution:
```
def diff_even_odd(lst):
    even = min(i for i in lst if i % 2 == 0)
    odd