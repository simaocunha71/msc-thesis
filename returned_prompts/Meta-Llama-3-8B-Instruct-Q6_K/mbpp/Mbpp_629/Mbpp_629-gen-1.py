You can use a list comprehension to filter out the even numbers from the list. Here's the solution:
```
def Split(lst):
    return [i for i in lst if i % 2 == 0]
```
This function iterates over each number in the list (`lst`) and checks if the remainder of the number divided by 2 is 0 (`i % 2 == 0`). If it is, the number is even and is added to the new list. The function then returns this new list of even numbers.

The unit test `assert Split([1,2,3,4,5]) == [2,4]` ensures that the function is working correctly by checking that the output of `Split([1,2,3,4,5])` is indeed `[2,4]`. If the function is working correctly, this test will pass. If the function is not working correctly, this test will fail, indicating that there is an error in the function. 