	res := 1
	
	for i := 1; i <= n; i++ {
		res *= i
	}
	
	for i := 1; i < n; i++ {
		res *= i
	}
	
	return res








```
import math

def SpecialFactorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    for i in range(1, n - 1):
        res *= i
    return res
```