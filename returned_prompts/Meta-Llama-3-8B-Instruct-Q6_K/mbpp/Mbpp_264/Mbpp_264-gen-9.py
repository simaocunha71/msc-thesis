```
def dog_age(years):
    return years * 5 + 21
```


The problem is asking to create a function that calculates a dog's age in dog years. The function should take the dog's age in human years as an argument and return the equivalent age in dog years.

The unit test `assert dog_age(12)==61` suggests that 12 years for a human is equivalent to 61 years for a dog. This is a common conversion factor used in the context of dogs, with the first year being equivalent to 15 human years, and each subsequent year being equivalent to 5 human years.

Here is the solution:
```
def dog_age(years):
    return years * 5 + 21
```
This function takes the dog's age in human years as an argument, multiplies it by 5 to account for the equivalent years in dog years, and then adds 21 to account for the first year being equivalent to 15 years. The result is the dog's age in dog years.