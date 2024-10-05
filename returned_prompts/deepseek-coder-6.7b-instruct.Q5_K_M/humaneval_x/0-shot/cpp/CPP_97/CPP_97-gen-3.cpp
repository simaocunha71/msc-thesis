  int last_digit_a, last_digit_b;
  last_digit_a = abs(a%10);
  last_digit_b = abs(b%10);
  return last_digit_a*last_digit_b;
}

int main() {
  printf("%d\n", multiply(148, 412)); // 16
  printf("%d\n", multiply(19, 28)); // 72
  printf("%d\n", multiply(2020, 1851)); // 0
  printf("%d\n", multiply(14,-15)); // 20
  return 0;
}


A: Here is a Python solution:

```python
def multiply(a, b):
    last_digit_a = abs(a) % 10
    last_digit_b = abs(b) % 10
    return last_digit_a * last_digit_b
```

This function works by first finding the last digit of each input number using the modulo operation (%). The modulo operation returns the remainder of a division, so `a % 10` gives the last digit of `a`, and `b % 10` gives the last digit of `b`.

The `abs` function is used to ensure that the last digit is always positive, even if the input number was negative.

Finally, the function returns the product of the last digits of `a` and `b`.

Here are some examples of how to use this function:

```python
print(multiply(148, 412))  # Output: 16
print(multiply(19, 28))  # Output: 72
print(multiply(2020, 1851))  # Output: 0
print(multiply(14, -15))  # Output: 20
```

This function should work correctly for any pair of integers.

Note: This code assumes that the input is always valid. If the input could be invalid (e.g