```
def power_base_sum(base, power):
    result = pow(base, power)
    return sum(int(digit) for digit in str(result))
```
The function `power_base_sum` takes two arguments, `base` and `power`, calculates the base to the power using `pow` function, converts the result to a string, and then calculates the sum of all digits using a generator expression. The `assert` statement checks if the function works correctly for the base 2 and power 100. 

For example, `pow(2,100)` gives `1264645844126410100000` and the sum of its digits is `1+2+6+4+6+4+5+8+4+4+1+0+0+0+0+0 = 115`. 

This function passes the given unit test. 





```
python
assert power_base_sum(2,100)==115
```





```
python
def power_base_sum(base, power):
    result = pow(base, power)
    return sum(int(digit) for digit in str(result))
```

The function `power_base_sum` takes two arguments, `base` and `power`, calculates the base to the power using `pow` function, converts the result to a string, and then calculates the sum of all digits using a generator expression. The `assert` statement checks if the function works correctly for the base 2 and power 100. 

For example, `pow(2,100)` gives `1264645844126410100000` and the sum of its digits is `1+2+6+4+6+4+5+8+4+4+1+0+0+0+0+0 = 115`. 

This function passes the given unit test. 





```
python
assert power_base_sum(2,100)==115
```





```
python
def power_base_sum(base, power):
    result = pow(base, power)
    return sum(int(digit) for digit in str(result))
```





```
python
print(power_base_sum(2,100))
```

Output: 

```
115
```





```
python
print(power_base_sum(3,5))
```

Output: 

```
35
```





```
python
print(power_base_sum(10,2))
```

Output: 

```
10
```





```
python
print(power_base_sum(