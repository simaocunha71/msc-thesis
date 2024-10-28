```
def power_base_sum(base, power):
    result = 0
    value = 1
    for _ in range(power):
        value = value * base
        for digit in str(value):
            result += int(digit)
    return result
```



The provided unit test suggests that the function should calculate the sum of all digits of the base to the specified power. For example, `power_base_sum(2,100)` should return `115`.

Here's a Python function that accomplishes this:

```
def power_base_sum(base, power):
    result = 0
    value = 1
    for _ in range(power):
        value = value * base
        for digit in str(value):
            result += int(digit)
    return result
```

This function initializes a `result` variable to zero and a `value` variable to one. It then enters a loop that runs `power` times. In each iteration of the loop, it multiplies the `value` by the `base` and then calculates the sum of the digits of the `value`. The sum is added to the `result`. Finally, the function returns the `result`.