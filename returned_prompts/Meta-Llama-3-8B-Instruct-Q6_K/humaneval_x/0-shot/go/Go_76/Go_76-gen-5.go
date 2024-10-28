```
return int(math.Pow(float64(n), float64(math.Log(float64(x))/math.Log(float64(n))))) == x
```


Here is the explanation:
- We use the math.Log function to calculate the logarithm of x and n.
- We divide the logarithm of x by the logarithm of n to get the power.
- We use the math.Pow function to raise n to the power we calculated.
- We compare the result with x. If they are equal, then x is a simple power of n.

This function works because the logarithm of a number raised to a power is equal to the power times the logarithm of the base. So, the logarithm of x divided by the logarithm of n gives us the power to which n should be raised to get x. Then, we raise n to that power and compare the result with x. If they are equal, then x is a simple power of n. If not, then it is not. This function is more efficient than the naive approach of iterating from 0 to x and checking if n^i = x, because it uses mathematical properties to calculate the power directly. It also works for large values of x and n, because it does not require storing the intermediate results of the power calculation.