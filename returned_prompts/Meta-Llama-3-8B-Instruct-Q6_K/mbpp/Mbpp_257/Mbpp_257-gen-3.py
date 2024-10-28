```
def swap_numbers(a, b):
    return (b, a)
```


This function takes two numbers, a and b, and returns a tuple with b as the first element and a as the second element. This is achieved by using the tuple constructor with the arguments b and a in that order. The unit test `assert swap_numbers(10,20)==(20,10)` shows that the function should swap the two numbers.