To solve this problem we need to write a function that sorts a list of tuples based on the second value of each tuple.

Here's a step-by-step guide on how to do it:

1. Define a function called `subject_marks` that takes in a list of tuples as a parameter.
2. Use the built-in `sorted` function to sort the list of tuples. Pass a lambda function as the `key` parameter to this `sorted` function. This lambda function will tell the `sorted` function to sort the tuples based on the second element of each tuple (i.e., `t[1]`).
3. Return the sorted list of tuples from the function.
4. Test the function by using the `assert` statement to check if the function returns the expected result.

Here's the code that implements these steps:

```python
def subject_marks(marks_list):
    sorted_marks_list = sorted(marks_list, key=lambda t: t[1])
    return sorted_marks_list
```

Now we can test the function with the provided example:

```python
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]) == [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
```

The `assert` statement checks if the result of the `subject_marks` function is equal to the expected result. If the result is correct, the `assert` statement will not raise an exception.

I hope this helps! Let me know if you have any further questions.

Additionally, it's important to note that the `sorted` function returns a new sorted list and does not modify the original list. This is because it is a built-in Python function and not a method of the list object.

Here's an example to demonstrate this:

```python
marks_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_marks_list =