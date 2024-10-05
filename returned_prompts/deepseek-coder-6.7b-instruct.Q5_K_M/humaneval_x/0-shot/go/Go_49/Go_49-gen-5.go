
	mod := 1<<p
	res := 1
	for n != 0 {
		if n&1 != 0 {
			res = (res * 2) % mod
		}
		n = n >> 1
	}
	return res - 1
}

func main() {
	fmt.Println(Modp(3, 5))
	fmt.Println(Modp(1101, 101))
	fmt.Println(Modp(0, 101))
	fmt.Println(Modp(3, 11))
	fmt.Println(Modp(100, 101))
}

```

This is a Python version of the same logic:

```python
def Modp(n, p):
    mod = 1 << p
    res = 1
    while(n > 0):
        if (n & 1):
            res = (res * 2) % mod
        n = n >> 1
    return res - 1

print(Modp(3, 5))
print(Modp(1101, 101))
print(Modp(0, 101))
print(Modp(3, 11))
print(Modp(100, 101))
```

Both codes calculate 2^n modulo p.

Explanation:

The code calculates 2^n modulo p by using bitwise shift and AND operations.

It first calculates 2^n using bitwise shift and AND operations.

Then it calculates the modulus of the result with respect to 2^p using bitwise shift operations.

Finally, it subtracts 1 from the result to get the correct modulus value.

Please note that the modulus operation is used to avoid overflow when n is large.
*/
package main

import (
	"fmt"
)

func Modp(n int, p int) int {
	mod := 1 << p
	res := 1
	for n != 0 {
		if n&1 != 0 {
			res = (res * 2) %