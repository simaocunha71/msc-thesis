```
def Split(input_list):
    output_list = []
    for i in input_list:
        if i % 2 == 1:
            output_list.append(i)
    return output_list
```

Explanation:
The function Split takes a list of integers as input and creates an empty list called output_list. It then iterates through each number in the input_list and checks whether it is odd or not by using the modulo operator (%). If the remainder after dividing the number by 2 is equal to 1, it means the number is odd, so it is added to the output_list. Finally, the function returns the output_list containing only the odd numbers.

The assert statement is used to verify if the function is correctly returning the expected output for the given test case. In this case, the expected output for the input list [1,2,3,4,5,6] is [1,3,5]. The assert statement checks if the function's output matches the expected output and raises an error if they are not equal.

Overall, this solution effectively filters out the odd numbers from the input list using a simple loop and conditional check.

Note: It's worth mentioning that a more concise and efficient solution can be achieved using list comprehension:

```python
def Split(input_list):
    return [i for i in input_list if i % 2 == 1]
```
This code does the same thing as the previous solution but in a more concise manner using a single line of code. It uses list comprehension to create a new list containing only the odd numbers from the input_list.

Both solutions achieve the same result, but the choice between them may depend on personal preference or specific requirements of the codebase.

Additionally, it's important to note that Python provides built-in methods like `filter()` and `map()` that can be used to achieve the same result in a more readable and efficient manner:

```python
def Split(input_list):
    return list(filter(lambda x: x % 2 == 1, input_list))
```
In this solution, the `filter()` function is used to iterate through the input_list