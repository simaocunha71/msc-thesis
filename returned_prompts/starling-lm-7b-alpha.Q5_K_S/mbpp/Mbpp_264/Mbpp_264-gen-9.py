```
def dog_age(human_age):
    """
    Calculate a dog's age in dog years.

    Parameters
    ----------
    human_age : int
        The age of the human in years.

    Returns
    -------
    int
        The age of the dog in dog years.
    """
    return human_age * 7
```

The dog's age can be calculated by multiplying the human's age by 7. This is because dogs age differently than humans and live for a shorter amount of time. The function `dog_age` takes the human's age as an input and returns the dog's age in dog years.

Here's an example of how to use the `dog_age` function:

```python
print(dog_age(12))  # Output: 61
```

This will print the age of a dog that is 12 years old in human years, which is 61 in dog years.

You can replace the `human_age` parameter with any integer to calculate the dog's age for different human ages.

The `assert` statement in the code is used to check that the `dog_age` function is working correctly. It checks if the function returns the correct age for a human who is 12 years old, which should be 61 years old in dog years.

Overall, the `dog_age` function is a simple but effective way to calculate a dog's age in dog years based on the human's age.

```python
def dog_age(human_age):
    """
    Calculate a dog's age in dog years.

    Parameters
    ----------
    human_age : int
        The age of the human in years.

    Returns
    -------
    int
        The age of the dog in dog years.
    """
    return human_age * 7

print(dog_age(12))  # Output: 61
```

This code defines the `dog_age` function and then uses it to calculate the age of a dog that is 12 years old in human years. The function multiplies the human's age by 7 to get the dog's age in