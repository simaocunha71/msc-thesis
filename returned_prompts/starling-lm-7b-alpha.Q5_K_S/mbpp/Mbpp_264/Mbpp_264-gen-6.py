"""
The first step to this problem is to understand that one dog year is approximately equal to seven human years. Therefore, we can divide the human age by seven to find the dog age. However, this would not account for the difference in growth rates between dogs and humans.

Here's a function that can perform these calculations:

```python
def dog_age(human_age):
    if human_age < 2:
        return human_age * 10.5
    else:
        return (human_age - 2) * 4 + 21
```

In this function, if the human age is less than 2, it means the dog is less than 14 in human years (since 2*10.5 = 21). Therefore, the function just returns the human age multiplied by 10.5. If the human age is equal to or greater than 2, it means the dog is 14 or older in human years. In this case, the function calculates the dog age as (human age - 2) * 4 + 21. This is because a dog's first year is the equivalent of a human year, but every following year after the first is calculated as four times the human age. The 21 is added to account for the first two human years.

For example, if you call `dog_age(12)`, it will return 61, which is the equivalent of 12 human years in dog years.

"""

def dog_age(human_age):
    if human_age < 2:
        return human_age * 10.5
    else:
        return (human_age - 2) * 4 + 21

def test_dog_age():
    assert dog_age(12) == 61

test_dog_age()

# It's important to note that the calculation of a dog's age in human years is an approximation and can vary depending on the breed, size, and individual characteristics of the dog.
```

```

```